/*
 * @Author: zhouyou@werun 
 * @Descriptions: 用户注册界面 
 * @Date: 2018-07-09 09:57:02 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 17:04:26
 */


<template>
    <div id="regist-box">
        <div id="regist-box-content">
            <div class="content">
                <a href="" @click.prevent="registBoxHide()">
                    <i class="el-icon-close"></i>
                </a>
                <h3>用户注册</h3>
                <div class="line">
                    <el-input v-model="defaultData.nickname" placeholder="请输入用户名" prefix-icon="el-icon-edit-outline"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="defaultData.password" type="password" placeholder="请输入密码" prefix-icon="el-icon-view"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="defaultData.phone" placeholder="请输入联系方式" prefix-icon="el-icon-mobile-phone"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="defaultData.email" placeholder="请输入注册邮箱" prefix-icon="el-icon-message"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="defaultData.name" placeholder="请输入姓名" prefix-icon="el-icon-edit-outline"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="defaultData.id_card" placeholder="请输入身份证号码" prefix-icon="el-icon-tickets"></el-input>
                </div>
                <div class="line">
                    <el-select v-model="defaultData.role_id" placeholder="请选择角色" class="select-box">
                        <el-option v-for="item in roles" :key="item.value" :label="item.label" :value="item.value">
                        </el-option>
                    </el-select>
                </div>
                <div class="line clearfix">
                    <el-checkbox v-model="checked" class="check-box">我已经阅读并同意
                        <a href="" @click.prevent="disclaimerToggle()">《寻房网服务协议》</a>
                    </el-checkbox>
                </div>
                <button @click="regist()">同意条款并注册</button>
            </div>
        </div>
        <transition name="fade">
            <disclaimer-box v-show="isDisclaimerShow" v-on:callback="disclaimerToggle()"></disclaimer-box>
        </transition>
        <div class="mask-layer"></div>
    </div>
</template>



<script>
import DisclaimerBox from "../components/DisclaimerBox";
import { hex_md5 } from "../js/md5.js";
import qs from "qs";

const RegistBox = {
    data: function() {
        return {
            roles: [
                {
                    value: 3,
                    label: "出租用户"
                },
                {
                    value: 4,
                    label: "租房用户"
                }
            ],

            defaultData: {
                nickname: "",
                password: "",
                email: "",
                phone: "",
                role_id: "",
                name: "",
                id_card: ""
            },

            checked: true,
            isDisclaimerShow: false
        };
    },
    components: {
        DisclaimerBox: DisclaimerBox
    },
    methods: {
        regist: function() {
            const self = this;

            if (
                !this.defaultData.nickname ||
                !this.defaultData.password ||
                !this.defaultData.email ||
                !this.defaultData.phone ||
                !this.defaultData.role_id ||
                !this.defaultData.name ||
                !this.defaultData.id_card
            ) {
                this.$message.error("输入选项不能为空，请检查后重新提交！");
                return;
            }

            this.defaultData.password = hex_md5(this.defaultData.password);

            // regist
            this.$axios
                .post("/c2c/regist", this.defaultData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        // regist success
                        self.$message({
                            message: "注册成功！",
                            type: "success"
                        });
                        self.$emit("callback");
                    } else {
                        // regist fail
                        self.$message.error("注册失败！");
                    }
                });
        },

        registBoxHide() {
            this.$emit("callback");
        },
        disclaimerToggle() {
            this.isDisclaimerShow = !this.isDisclaimerShow;
        }
    }
};

export default RegistBox;
</script>


<style lang="scss" scoped>
#regist-box-content {
    position: absolute;
    z-index: 12;
    top: 100px;
    left: 0;
    right: 0;
    margin: 0 auto;
    width: 450px;
    border-radius: 20px;
    background: #fff;

    .content {
        position: relative;
        padding: 20px 30px 30px;

        a:hover {
            color: #ff5a5f;
        }

        .el-icon-close {
            position: absolute;
            top: 10px;
            right: 10px;
            font-size: 30px;
        }

        h3 {
            font-size: 24px;
        }

        .line {
            margin-bottom: 20px;

            .select-box {
                width: 390px;
            }

            .check-box {
                float: left;
            }
        }
        button {
            border: none;
            border-radius: 5px;
            width: 390px;
            height: 40px;
            background: #ff5a5f;
            color: #fff;
        }
    }
}
</style>



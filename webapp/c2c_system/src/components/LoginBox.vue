/*
 * @Author: zhouyou@werun 
 * @Descriptions: 用户登录界面 
 * @Date: 2018-07-09 09:57:25 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 19:19:00
 */


<template>
    <div id="login-box">
        <div id="login-box-content">
            <div class="content">
                <a href="" @click.prevent="closeLoginBox()">
                    <i class="el-icon-close"></i>
                </a>
                <h3>用户登录</h3>
                <div class="line">
                    <el-input v-model="userEmail" placeholder="请输入登录邮箱" prefix-icon="el-icon-edit-outline"></el-input>
                </div>
                <div class="line">
                    <el-input v-model="password" type="password" placeholder="请输入密码" prefix-icon="el-icon-view"></el-input>
                </div>
                <button @click="login()">登录</button>
            </div>
        </div>
        <div class="mask-layer"></div>
    </div>
</template>



<script>
import qs from "qs";
import { hex_md5 } from "../js/md5.js";
import { mapActions } from "vuex";

const LoginBox = {
    data: function() {
        return {
            userEmail: "",
            password: ""
        };
    },
    methods: {
        ...mapActions(["updateUserId"]),
        login: function() {
            const self = this;

            //judge empty
            if (!this.userEmail || !this.password) {
                this.$message.error("登录邮箱或密码不能为空");
                return;
            }

            var postData = {
                email: this.userEmail,
                password: hex_md5(this.password)
            };

            // self.$cookie.setCookie("c2c_user_id", 4);

            // login
            this.$axios.post("/c2c/login", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    // login success
                    self.$cookie.setCookie("c2c_user_id", data.user_id);
                    self.$message({
                        message: "登录成功！",
                        type: "success"
                    });
                    self.$emit("callback");
                    self.updateUserId();
                } else {
                    // login fail
                    self.$message.error("登录失败");
                }
            });
        },

        closeLoginBox: function() {
            this.$emit("callback");
        }
    }
};

export default LoginBox;
</script>


<style lang="scss" scoped>
#login-box-content {
    position: absolute;
    z-index: 13;
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


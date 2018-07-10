/*
 * @Author: zhouyou@werun 
 * @Descriptions: 个人资料页面 
 * @Date: 2018-07-06 14:03:28 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 10:32:22
 */


<template>
    <div id="personal-data-page">
        <div class="line">
            <h2>个人资料</h2>
        </div>
        <div class="line input-box">
            <span>用户名</span>
            <el-input v-model="defaultData.nickname" placeholder="请输入用户名"></el-input>
        </div>
        <div class="line input-box">
            <span>邮箱</span>
            <el-input v-model="defaultData.email" placeholder="请输入邮箱" disabled></el-input>
        </div>
        <div class="line input-box">
            <span>手机号</span>
            <el-input v-model="defaultData.phone" placeholder="请输入手机号"></el-input>
        </div>
        <div class="line input-box">
            <span>居住地址</span>
            <el-input placeholder="请输入居住地址"></el-input>
        </div>
        <div class="line text-box">
            个人介绍
            <br>
            <br>
            <el-input v-model="defaultData.info" type="textarea" placeholder="请输入个人介绍"></el-input>
        </div>
        <div class="button-container">
            <button class="common-button" @click.prevent="updatePersonalInformation()">确认提交</button>
        </div>
    </div>
</template>


<script>
import { mapGetters } from "vuex";

const PersonalDataPage = {
    data: function() {
        return {
            type: 0,
            options: [{ value: 0, label: "公寓" }, { value: 1, label: "民宿" }],

            defaultData: {
                address: null,
                email: "",
                id_card: "",
                name: "",
                nickname: "",
                phone: "",
                user_id: "",
                info: ""
            }
        };
    },
    computed: {
        ...mapGetters["userId"]
    },
    methods: {
        getPersonalInformation: function() {
            const self = this;

            // get user info
            this.$axios.post("/c2c/userinfo").then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.defaultData = data;
                } else {
                    // get fail
                    self.$message.error("获取失败");
                }
            });
        },

        // update user info
        updatePersonalInformation: function() {
            const self = this;

            // update
            this.$axios
                .post("/c2c/userupdate", this.defaultData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.$message({
                            message: "更新成功！",
                            type: "success"
                        });
                    } else {
                        // update fail
                        self.$message.error("提交失败");
                    }
                });
        }
    },
    created() {
        this.getPersonalInformation();
    }
};

export default PersonalDataPage;
</script>


<style lang="scss">
#personal-data-page {
    padding: 30px;
    text-align: left;
    margin-bottom: 50px;

    .line {
        padding: 20px 0 20px;
        border-bottom: 1px solid #bbb;

        span {
            display: inline-block;
            width: 80px;
        }

        .el-input {
            margin-left: 20px;
        }
    }

    .input-box {
        .el-input {
            width: 300px;
            margin-left: 20px;
        }

        input {
            width: 220px;
            height: 40px;
        }
    }

    .text-box {
        .el-input {
            width: 300px;
            margin-left: 20px;
        }

        textarea {
            width: 740px;
            height: 100px;
        }
    }

    .button-container {
        text-align: center;

        .common-button {
            margin-top: 35px;
            width: 150px;
            height: 40px;
            font-size: 16px;
        }
    }
}
</style>

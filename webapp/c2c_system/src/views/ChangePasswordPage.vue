/*
 * @Author: zhouyou@werun 
 * @Descriptions: 修改界面 
 * @Date: 2018-07-06 14:11:14 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 10:46:55
 */


<template>
    <div id="change-password-page">
        <div class="line">
            <h2>修改密码</h2>
        </div>
        <div class="line input-box">
            <span>旧密码</span>
            <el-input type="password" v-model="oldPassword" placeholder="请输入旧密码"></el-input>
        </div>
        <div class="line input-box">
            <span>新密码</span>
            <el-input type="password" v-model="newPassword" placeholder="请输入新密码"></el-input>
        </div>
        <div class="line input-box">
            <span>确认新密码</span>
            <el-input type="password" v-model="newPassword2" placeholder="请再次输入密码"></el-input>
        </div>
        <div class="button-container">
            <button class="common-button" @click="commit()">确认修改</button>
        </div>
    </div>
</template>


<script>
import { hex_md5 } from "../js/md5.js";

const ChangePasswordPage = {
    data: function() {
        return {
            oldPassword: "",
            newPassword: "",
            newPassword2: ""
        };
    },
    methods: {
        commit: function() {
            const self = this;

            if (this.newPassword !== this.newPassword2) {
                self.$message.error("两次输入的密码不一致！");
                return;
            }

            var postData = {
                old_password: hex_md5(this.oldPassword),
                password: hex_md5(this.newPassword)
            };

            // update
            this.$axios
                .post("/c2c/changepassword", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.$message({
                            message: "修改成功！",
                            type: "success"
                        });
                        location.reload();
                    } else {
                        // update fail
                        self.$message.error(data.error);
                    }
                });
        }
    }
};

export default ChangePasswordPage;
</script>


<style lang="scss">
#change-password-page {
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


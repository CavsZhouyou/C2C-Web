/*
 * @Author: zhouyou@werun 
 * @Descriptions: 个人资料页面 
 * @Date: 2018-07-06 14:03:28 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 15:46:25
 */


<template>
    <div id="personal-data-page">

        <div class="line">
            <h2>个人资料</h2>
        </div>
        <div class="line head-img">
            <span>用户头像</span>
            <img :src="defaultData.headico">
            <button class="common-button">上传头像</button>
            <input type="file" required accept="image/png, image/jpeg, image/gif, image/jpg" id="photoUploadBtn" @change="uploadPhoto">
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
        <!-- <div class="line input-box">
            <span>居住地址</span>
            <el-input placeholder="请输入居住地址"></el-input>
        </div> -->
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
import { mapActions } from "vuex";
import * as qiniu from "qiniu-js";

const defaultHeadImg = require("../assets/head-img.jpg");

const PersonalDataPage = {
    data: function() {
        return {
            type: 0,
            options: [{ value: 0, label: "公寓" }, { value: 1, label: "民宿" }],

            defaultData: {
                headico: defaultHeadImg,
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
        ...mapActions(["updateHeadImg"]),

        uploadPhoto: function(event) {
            const self = this;
            this.$axios.post("/c2c/upload").then(function(response) {
                var data = response.data;
                if (data.success) {
                    var observable = qiniu.upload(
                        event.target.files[0],
                        data.key,
                        data.token
                    );

                    var observer = {
                        next(res) {},
                        error(err) {},
                        complete(res) {
                            var photoUrl =
                                "http://" + data.domain + "/" + res.key;
                            self.defaultData.headico = photoUrl;
                        }
                    };

                    var subscription = observable.subscribe(observer); // 上传开始
                }
            });
        },
        getPersonalInformation: function() {
            const self = this;

            // get user info
            this.$axios.post("/c2c/userinfo").then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.defaultData = data;

                    if (!data.headico) {
                        self.defaultData.headico = defaultHeadImg;
                    }
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
                        self.updateHeadImg(self.defaultData.headico);
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

    .head-img {
        img {
            margin-left: 20px;
            margin-right: 20px;
            width: 100px;
            height: 100px;
            vertical-align: middle;
        }

        .common-button {
            width: 100px;
            height: 30px;
            border-radius: 10px;
            vertical-align: bottom;
        }

        #photoUploadBtn {
            position: absolute;
            margin-top: 71px;
            margin-left: -100px;
            width: 100px;
            height: 30px;
            opacity: 0;
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

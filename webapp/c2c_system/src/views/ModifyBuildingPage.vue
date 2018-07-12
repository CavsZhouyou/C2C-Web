/*
 * @Author: zhouyou@werun 
 * @Descriptions: 修改房源信息 
 * @Date: 2018-07-11 17:08:36 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-12 11:43:30
 */

<template>
    <div id="modify-building-page">
        <div class="line">
            <h2>房源信息修改</h2>
        </div>
        <div class="line">
            房源类型
            <el-select v-model="defaultData.acc_type" placeholder="请选择房源类型">
                <el-option v-for="item in typeOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line input-box">
            房源大小
            <el-input v-model="defaultData.acc_capacity" placeholder="请输入房源大小"></el-input>
        </div>
        <div class="line input-box">
            房源地址
            <el-select v-model="defaultData.acc_city" placeholder="城市" class="select-box" @change="getCounty()">
                <el-option v-for="item in cityOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="defaultData.acc_county" placeholder="区/县" class="select-box" @change="getStreet()">
                <el-option v-for="item in countyOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="defaultData.acc_street" placeholder="街道/镇" class="select-box">
                <el-option v-for="item in streetOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-input v-model="defaultData.acc_address" placeholder="请输入详细地址"></el-input>
        </div>
        <div class="line input-box">
            出租价格
            <el-input v-model="defaultData.acc_price" placeholder="请输入出租价格"></el-input>
            <el-select v-model="unit" placeholder="请选择单位" class="select-box">
                <el-option v-for="item in unitOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line text-box">
            房源详细介绍
            <br>
            <br>
            <el-input v-model="defaultData.acc_description" type="textarea" placeholder="请输入房源详细介绍"></el-input>
        </div>
        <div class="line text-box photo-attachments">
            房源图片添加
            <br>
            <br>
            <div class="container">
                <div class="img-box" v-for="(photoUrl,index) in pictureUrls" :key="index">
                    <img :src="photoUrl" class="photo" alt="附件图片" title="附件图片">
                    <img src="../assets/del.png" class="delete" alt="删除图片" title="删除图片" @click="deletePhoto(index)">
                </div>
                <div id="add-photo">
                    <img src="../assets/add-photo.png" class="add-photo">
                    <input type="file" required accept="image/png, image/jpeg, image/gif, image/jpg" id="photoUploadBtn" @change="uploadPhoto">
                </div>
            </div>
        </div>
        <div class="button-container">
            <button class="common-button" @click="commit()">修改房源信息</button>
        </div>
    </div>
</template>


<script>
import * as qiniu from "qiniu-js";
import { mapGetters } from "vuex";

const ModifyBuildingPage = {
    data: function() {
        return {
            type: "",
            typeOptions: [
                { value: 1, label: "公寓" },
                { value: 2, label: "民宿" },
                { value: 3, label: "客栈" },
                { value: 4, label: "酒店" },
                { value: 5, label: "独栋别墅" }
            ],
            unit: 1,
            unitOptions: [{ value: 1, label: "日" }],
            city: "",
            cityOptions: [],
            county: "",
            countyOptions: [],
            street: "",
            streetOptions: [],
            pictureUrls: [],

            defaultData: {
                acc_type_id: "",
                acc_capacity: "",
                acc_city: "",
                acc_county: "",
                acc_street: "",
                acc_address: "",
                acc_price: "",
                acc_description: "",
                acc_images: "",
                acc_datetype: 1
            }
        };
    },
    methods: {
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
                            self.pictureUrls.push(photoUrl);
                        }
                    };

                    var subscription = observable.subscribe(observer); // 上传开始
                }
            });
        },

        deletePhoto: function(index) {
            this.pictureUrls.splice(index, 1);
        },
        commit: function() {
            const self = this;

            var postData = this.defaultData;

            postData.acc_images = this.pictureUrls.join(" ");
            postData.acc_type_id = postData.acc_type;

            // update
            this.$axios
                .post("/c2c/accommodation/update", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.$message({
                            message: "修改成功！",
                            type: "success"
                        });
                        self.$router.push(
                            "/PersonalCenterPage/ViewBuildingPage"
                        );
                        // location.reload();
                    } else {
                        // update fail
                        self.$message.error("修改失败");
                    }
                });
        },

        getCity: function() {
            const self = this;

            this.$axios.post("/c2c/city").then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.cityOptions = data.citys;
                }
            });
        },
        getCounty: function() {
            const self = this;

            var postData = {
                city_id: this.defaultData.acc_city
            };

            this.$axios.post("/c2c/county", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.countyOptions = data.counties;
                }
            });
        },
        getStreet: function() {
            const self = this;

            var postData = {
                county_id: this.defaultData.acc_county
            };

            this.$axios.post("/c2c/street", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.streetOptions = data.streets;
                }
            });
        },

        getBuildingInformation: function() {
            const self = this;

            var postData = {
                acc_id: this.$route.params.buildingId
            };

            this.$axios
                .post("/c2c/accommodation/show", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.defaultData = data;
                        self.pictureUrls = data.acc_images;
                        self.getCounty();
                        self.getStreet();
                    }
                });
        }
    },

    created() {
        this.getCity();
        this.getBuildingInformation();
    }
};

export default ModifyBuildingPage;
</script>


<style lang="scss">
#modify-building-page {
    padding: 30px;
    text-align: left;
    margin-bottom: 50px;

    .line {
        padding: 20px 0 20px;
        border-bottom: 1px solid #bbb;

        .el-input {
            margin-left: 20px;
        }
    }

    .input-box {
        .el-input {
            width: 220px;
            margin-left: 20px;
        }

        input {
            width: 220px;
            height: 40px;
        }

        .select-box {
            width: 120px;
            margin-right: 10px;

            .el-input {
                width: 120px;
                margin-left: 20px;
            }

            input {
                width: 120px;
            }
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

    .photo-attachments {
        margin-top: 30.0096px;

        .container {
            width: 850.0032px;
            padding: 20.0064px;
            padding-left: 0px;

            .img-box {
                display: inline-block;
                width: 300px;
                height: 169.9968px;
                margin-left: 50.0736px;
                margin-right: 30px;
                margin-bottom: 20.0064px;

                .photo {
                    width: 300px;
                    height: 169.9968px;
                }

                .delete {
                    position: absolute;
                    margin-top: -13.3568px;
                    margin-left: -13px;
                }
            }

            #add-photo {
                display: inline-block;
                position: relative;
                margin-left: 100.0736px;
                width: 169.9968px;
                height: 169.9968px;
                text-align: center;

                img {
                    position: absolute;
                    z-index: 15;
                    top: 0;
                    left: 0;
                    width: 144.768px;
                    height: 144.768px;
                }

                .select-photo {
                    position: absolute;
                    z-index: 16;
                    top: 124.8px;
                    left: 94.2336px;
                    color: #1296db;
                }

                #photoUploadBtn {
                    position: absolute;
                    z-index: 16;
                    top: 0;
                    left: 0;
                    width: 144.768px;
                    height: 144.768px;
                    opacity: 0;
                    cursor: pointer;
                }
            }
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

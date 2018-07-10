/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布房源信息 
 * @Date: 2018-07-06 12:57:17 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 20:32:28
 */


<template>
    <div id="release-building-page">
        <div class="line">
            <h2>房源信息发布</h2>
        </div>
        <div class="line">
            房源类型
            <el-select v-model="type" placeholder="请选择房源类型">
                <el-option v-for="item in typeOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line input-box">
            房源大小
            <el-input placeholder="请输入房源大小"></el-input>
        </div>
        <div class="line input-box">
            房源地址
            <el-select v-model="city" placeholder="城市" class="select-box">
                <el-option v-for="item in cityOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="town" placeholder="区/县" class="select-box">
                <el-option v-for="item in townOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-select v-model="street" placeholder="街道/镇" class="select-box">
                <el-option v-for="item in streetOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
            <el-input placeholder="请输入详细地址"></el-input>
        </div>
        <div class="line input-box">
            出租价格
            <el-input placeholder="请输入出租价格"></el-input>
            <el-select v-model="unit" placeholder="请选择单位" class="select-box">
                <el-option v-for="item in unitOptions" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line text-box">
            房源详细介绍
            <br>
            <br>
            <el-input type="textarea" placeholder="请输入房源详细介绍"></el-input>
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
            <button class="common-button" @click="commit">发布房源信息</button>
        </div>
    </div>
</template>


<script>
import * as qiniu from "qiniu-js";

const ReleaseBuildingPage = {
    data: function() {
        return {
            type: "",
            typeOptions: [
                { value: 1, label: "公寓" },
                { value: 2, label: "民宿" },
                { value: 3, label: "宾馆" }
            ],
            unit: "",
            unitOptions: [
                { value: 1, label: "日" },
                { value: 2, label: "月" },
                { value: 3, label: "年" }
            ],
            city: "",
            cityOptions: [
                { value: 1, label: "威海市" },
                { value: 2, label: "北京市" },
                { value: 3, label: "重庆市" }
            ],
            town: "",
            townOptions: [
                { value: 1, label: "环翠区" },
                { value: 2, label: "荣成市" },
                { value: 3, label: "乳山市" },
                { value: 4, label: "文登区" },
                { value: 5, label: "其他区" }
            ],
            street: "",
            streetOptions: [
                { value: 1, label: "怡园街道" },
                { value: 2, label: "张村镇" },
                { value: 3, label: "温泉镇" },
                { value: 4, label: "西苑街道" },
                { value: 5, label: "竹岛街道" }
            ],
            photoList: [
                {
                    name: "food.jpeg",
                    url:
                        "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100"
                }
            ],
            pictureUrls: []
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
                            var photoUrl = data.domain + "/" + res.key;
                            var photo = require(photoUrl);
                            self.pictureUrls.push(photo);
                        }
                    };

                    var subscription = observable.subscribe(observer); // 上传开始
                }
            });
        },
        commit: function() {
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

export default ReleaseBuildingPage;
</script>


<style lang="scss">
#release-building-page {
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
                margin-bottom: 20.0064px;

                .photo {
                    width: 300px;
                    height: 169.9968px;
                }

                .delete {
                    position: absolute;
                    margin-top: -185.3568px;
                    margin-left: 288px;
                }
            }

            #add-photo {
                display: inline-block;
                position: relative;
                // margin-left: 50.0736px;
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

/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布房源信息 
 * @Date: 2018-07-06 12:57:17 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 13:45:22
 */


<template>
    <div id="release-building-page">
        <div class="line">
            <h2>房源信息发布</h2>
        </div>
        <div class="line">
            房源类型
            <el-select v-model="type" placeholder="">
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line input-box">
            房源大小
            <el-input placeholder="请输入房源大小"></el-input>
        </div>
        <div class="line input-box">
            房源地址
            <el-input placeholder="请输入房源地址"></el-input>
        </div>
        <div class="line input-box">
            出租价格
            <el-input placeholder="请输入出租价格"></el-input>
        </div>
        <div class="line text-box">
            房源详细介绍
            <br>
            <br>
            <el-input type="textarea" placeholder="请输入房源详细介绍"></el-input>
        </div>
        <div class="line text-box">
            房源图片添加
            <br>
            <br>
            <el-upload class="upload-demo" action="https://jsonplaceholder.typicode.com/posts/" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList2" list-type="picture">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload>
        </div>
        <div class="button-container">
            <button class="common-button">发布房源信息</button>
        </div>
    </div>
</template>


<script>
const ReleaseBuildingPage = {
    data: function() {
        return {
            type: 0,
            options: [{ value: 0, label: "公寓" }, { value: 1, label: "民宿" }],
            fileList2: [
                {
                    name: "food.jpeg",
                    url:
                        "https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100"
                }
            ]
        };
    },
    methods: {
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            this.fileList2.push(file);
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

/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布预定订单页面 
 * @Date: 2018-07-06 12:57:17 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 21:03:42
 */


<template>
    <div id="release-order-page">
        <div class="line">
            <h2>预定订单</h2>
        </div>
        <div class="line input-box">
            <span>出租者姓名</span>
            <el-input placeholder="请输入出租者姓名"></el-input>
        </div>
        <div class="line input-box">
            <span>出租者身份证</span>

            <el-input placeholder="请输入出租者身份证"></el-input>
        </div>
        <div class="line input-box">
            <span>租户姓名</span>
            <el-input placeholder="请输入租户姓名"></el-input>
        </div>
        <div class="line input-box">
            <span>租户身份证</span>
            <el-input placeholder="请输入租户身份证"></el-input>
        </div>
        <div class="line">
            <span>房源类型</span>
            <el-select v-model="type" placeholder="">
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line input-box">
            <span> 房源大小</span>
            <el-input placeholder="请输入房源大小"></el-input>
        </div>
        <div class="line input-box">
            <span> 房源地址</span>
            <el-input placeholder="请输入房源地址"></el-input>
        </div>
        <div class="line input-box">
            <span>成交价格</span>
            <el-input placeholder="请输入成交价格"></el-input>
        </div>
        <div class="line">
            <span>租房日期</span>
            <el-date-picker v-model="value6" type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期">
            </el-date-picker>
        </div>
        <div class="line text-box">
            备注
            <br>
            <br>
            <el-input type="textarea" placeholder="备注"></el-input>
        </div>
        <div class="button-container">
            <button class="common-button">确认预定订单</button>
        </div>
    </div>
</template>


<script>
const ReleaseOrderPage = {
    data: function() {
        return {
            type: 0,
            options: [{ value: 0, label: "公寓" }, { value: 1, label: "民宿" }],
            value6: ""
        };
    }
};

export default ReleaseOrderPage;
</script>


<style lang="scss">
#release-order-page {
    padding: 30px;
    text-align: left;
    margin-bottom: 50px;

    .line {
        padding: 20px 0 20px;
        border-bottom: 1px solid #bbb;

        span {
            display: inline-block;
            width: 120px;
        }
    }

    .input-box {
        .el-input {
            width: 300px;
        }

        input {
            width: 220px;
            height: 40px;
        }
    }

    .text-box {
        .el-input {
            width: 300px;
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

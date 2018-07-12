/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布预定订单页面 
 * @Date: 2018-07-06 12:57:17 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 21:39:10
 */


<template>
    <div id="release-order-page">
        <div class="line">
            <h2>预定订单</h2>
        </div>
        <div class="line input-box">
            <span>出租者姓名</span>
            <el-input v-model="defaultData.lessor_name" placeholder="请输入出租者姓名" disabled></el-input>
        </div>
        <div class="line input-box">
            <span>出租者身份证</span>

            <el-input v-model="defaultData.lessor_id_card" placeholder="请输入出租者身份证" disabled></el-input>
        </div>
        <div class="line input-box">
            <span>租户姓名</span>
            <el-input v-model="defaultData.tenant_name" placeholder="请输入租户姓名" disabled></el-input>
        </div>
        <div class="line input-box">
            <span>租户身份证</span>
            <el-input v-model="defaultData.tenant_id_card" placeholder="请输入租户身份证" disabled></el-input>
        </div>
        <div class="line">
            <span>房源类型</span>
            <el-select v-model="defaultData.acc_type" placeholder="" disabled>
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
            </el-select>
        </div>
        <div class="line input-box">
            <span> 房源大小</span>
            <el-input v-model="defaultData.acc_capacity" placeholder="请输入房源大小" disabled></el-input>
        </div>
        <div class="line input-box address">
            <span> 房源地址</span>
            <el-input v-model="defaultData.acc_address" placeholder="请输入房源地址" disabled></el-input>
        </div>
        <div class="line">
            <span>租房日期</span>
            <el-date-picker v-model="dateRange" type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" @change="getPrice()">
            </el-date-picker>
        </div>
        <div class="line input-box">
            <span>成交价格</span>
            <el-input v-model="price" placeholder="请输入成交价格"></el-input>
        </div>
        <div class="line text-box">
            备注
            <br>
            <br>
            <el-input v-model="demand" type="textarea" placeholder="备注"></el-input>
        </div>
        <div class="button-container">
            <button class="common-button" @click="commit()">发布预定订单</button>
        </div>
    </div>
</template>


<script>
const ReleaseOrderPage = {
    data: function() {
        return {
            type: 0,
            options: [
                { value: 1, label: "公寓" },
                { value: 2, label: "民宿" },
                { value: 3, label: "客栈" },
                { value: 4, label: "酒店" },
                { value: 5, label: "独栋别墅" }
            ],
            dateRange: [],

            defaultData: {},
            price: "",
            demand: ""
        };
    },
    methods: {
        getOrderInformation: function() {
            const self = this;

            var postData = {
                acc_id: this.$route.params.buildingId
            };

            this.$axios
                .post("/c2c/reservation/request", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.defaultData = data;
                    }
                });
        },

        getPrice: function() {
            var time =
                (Date.parse(this.dateRange[1]) -
                    Date.parse(this.dateRange[0])) /
                86400000;
            this.price = time * parseInt(this.defaultData.price);
        },

        commit: function() {
            const self = this;

            var postData = {
                acc_id: this.$route.params.buildingId,
                price: this.price,
                begin: Date.parse(this.dateRange[0]),
                end: Date.parse(this.dateRange[1]),
                demand: this.demand
            };

            this.$axios
                .post("/c2c/reservation/add", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.$message({
                            message: "发布成功！",
                            type: "success"
                        });
                        self.$router.push(
                            "/PersonalCenterPage/ViewAllOrdersPage"
                        );
                    }
                });
        }
    },
    created() {
        this.getOrderInformation();
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

    .address {
        .el-input {
            width: 600px;
        }

        input {
            width: 400px;
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

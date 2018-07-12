/*
 * @Author: zhouyou@werun 
 * @Descriptions: 查看已发布房源
 * @Date: 2018-07-06 12:37:43 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-12 15:18:03
 */


<template>
    <div id="view-building-page">
        <div class="line">
            <h2>查看已发布房源</h2>
        </div>
        <div class="container">

            <div v-for="(building, index) in buildingList" :key="index" class="line order">
                <div class="left-bar">
                    <img :src="building.acc_images" class="head-img" @click="viewBuildingDetail(building.acc_id)">
                    <br> &nbsp;&nbsp;&nbsp;
                    <span>房屋类型：{{building.acc_type_name}}</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>房屋面积：{{building.acc_capacity}}m2</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <br>
                    <br>&nbsp;&nbsp;&nbsp;
                    <span>房屋地址：{{building.acc_city}}{{building.acc_county}}{{building.acc_street}}{{building.acc_address}}</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <br>&nbsp;&nbsp;&nbsp;
                    <p class="info">
                        房屋介绍： {{building.acc_description}}
                    </p>
                    <span class="modify">
                        <i class="el-icon-circle-check"></i>
                        <a href="" @click.prevent="modify(building.acc_id)">修改信息</a>
                    </span>
                    <el-button class="delete" type="text" @click="deleteUser(building.acc_id, index)">
                        <i class="el-icon-circle-close"></i>&nbsp;删除房源</el-button>
                </div>
            </div>
            <div class="load" @click="getBuildingList" v-show="!isEnd">
                加载更多
            </div>
            <!-- <div class="line order">
                <div class="left-bar">
                    <img src="../assets/1.png" class="head-img">
                    <br> &nbsp;&nbsp;&nbsp;
                    <span>房屋信息：</span>&nbsp;&nbsp;
                    <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>最多住2人</span>
                    <br>&nbsp;&nbsp;&nbsp;
                    <p class="info">
                        欢迎来到DUDUSA 1.<br>这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) ......
                    </p>
                    <span class="delete">
                        <i class="el-icon-circle-close"></i>
                        <a href="">删除房源</a>
                    </span>
                    <span class="modify">
                        <i class="el-icon-circle-check"></i>
                        <a href="">修改信息</a>
                    </span>
                </div>
            </div>
            <div class="line order">
                <div class="left-bar">
                    <img src="../assets/2.png" class="head-img">
                    <br> &nbsp;&nbsp;&nbsp;
                    <span>房屋信息：</span>&nbsp;&nbsp;
                    <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>最多住2人</span>
                    <br>&nbsp;&nbsp;&nbsp;
                    <p class="info">
                        欢迎来到DUDUSA 1.<br>这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) ......
                    </p>
                    <span class="delete">
                        <i class="el-icon-circle-close"></i>
                        <a href="">删除房源</a>
                    </span>
                    <span class="modify">
                        <i class="el-icon-circle-check"></i>
                        <a href="">修改信息</a>
                    </span>
                </div>
            </div>
            <div class="line order">
                <div class="left-bar">
                    <img src="../assets/3.png" class="head-img">
                    <br> &nbsp;&nbsp;&nbsp;
                    <span>房屋信息：</span>&nbsp;&nbsp;
                    <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                    <span>最多住2人</span>
                    <br>&nbsp;&nbsp;&nbsp;
                    <p class="info">
                        欢迎来到DUDUSA 1.<br>这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) ......
                    </p>
                    <span class="delete">
                        <i class="el-icon-circle-close"></i>
                        <a href="">删除房源</a>
                    </span>
                    <span class="modify">
                        <i class="el-icon-circle-check"></i>
                        <a href="">修改信息</a>
                    </span>
                </div>
            </div>
            <div class="line order"> -->
            <!-- <div class="left-bar">
                <img src="../assets/13.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>&nbsp;&nbsp;&nbsp;
                <p class="info">
                    欢迎来到DUDUSA 1.<br>这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) ......
                </p>
                <span class="delete">
                    <i class="el-icon-circle-close"></i>
                    <a href="">删除房源</a>
                </span>
                <span class="modify">
                    <i class="el-icon-circle-check"></i>
                    <a href="">修改信息</a>
                </span>
            </div> -->
            <!-- </div> -->
        </div>
    </div>
</template>


<script>
const ViewBuildingPage = {
    data: function() {
        return {
            buildingList: [],
            start: 0,
            isEnd: false
        };
    },
    methods: {
        getBuildingList: function() {
            const self = this;

            var postData = {
                index: this.start,
                count: 5
            };

            this.$axios
                .post("/c2c/accommodation/list", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.buildingList = self.buildingList.concat(data.list);
                        self.start += 5;

                        if (data.empty) {
                            self.isEnd = true;
                        }
                    }
                });
        },

        modify: function(id) {
            this.$router.push("/PersonalCenterPage/ModifyBuildingPage/" + id);
        },

        deleteUser: function(accId, index) {
            const self = this;

            this.$confirm("确认删除此房源信息吗?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning"
            })
                .then(() => {
                    var postData = {
                        acc_id: accId
                    };

                    this.$axios
                        .post("/c2c/accommdation/delete", postData)
                        .then(function(response) {
                            var data = response.data;
                            if (data.success) {
                                self.buildingList.splice(index, 1);
                                self.start = self.start - 1;
                                self.$message({
                                    message: "删除成功！",
                                    type: "success"
                                });
                            } else {
                                self.$message.error("删除失败！");
                            }
                        });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除"
                    });
                });
        },

        viewBuildingDetail: function(buildingId) {
            this.$router.push("/HouseDetailPage/" + buildingId);
        }
    },
    created() {
        this.getBuildingList();
    }
};

export default ViewBuildingPage;
</script>


<style lang="scss" scoped>
#view-building-page {
    padding: 30px;
    text-align: left;

    .line {
        border-bottom: 1px solid #bbb;
    }

    .container {
        .order {
            min-height: 100px;
            padding: 20px 0 20px;
            font-size: 14px;

            .left-bar {
                padding-left: 160px;

                .head-img {
                    position: absolute;
                    margin-left: -160px;
                    width: 150px;
                    height: 100px;
                }

                .info {
                    display: inline-block;
                    height: 40px;
                    width: 400px;
                    overflow: hidden;
                    text-overflow: ellipsis;
                    -webkit-box-orient: vertical;
                }

                .delete {
                    position: absolute;
                    margin-left: 35px;
                    padding: 0;
                    // margin-top: -45px;
                    color: #e51c23;

                    a {
                        color: #e51c23;
                    }
                }

                .modify {
                    position: absolute;
                    margin-left: 35px;
                    margin-top: -45px;
                    color: #3498db;

                    a {
                        color: #3498db;
                    }
                }
            }
        }

        .load {
            text-align: center;
            font-style: italic;
            font-size: 20.9984px;
            color: #c5c5c5;
            cursor: pointer;
        }
    }
}
</style>


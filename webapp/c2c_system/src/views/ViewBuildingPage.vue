/*
 * @Author: zhouyou@werun 
 * @Descriptions: 查看已发布房源/*
 * @Author: zhouyou@werun 
 * @Descriptions: 查看房源订单页面 
 * @Date: 2018-07-06 12:37:43 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 12:55:24
 */


<template>
    <div id="view-building-page">
        <div class="line">
            <h2>查看已发布房源</h2>
        </div>
        <div class="line order">
            <div class="left-bar">
                <img src="../assets/1.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
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
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
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
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
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
                <img src="../assets/13.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
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
    </div>
</template>


<script>
const ViewBuildingPage = {};

export default ViewBuildingPage;
</script>


<style lang="scss" scoped>
#view-building-page {
    padding: 30px;
    text-align: left;

    .line {
        border-bottom: 1px solid #bbb;
    }

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

            .delete {
                position: absolute;
                margin-left: 80px;
                margin-top: -45px;
                color: #e51c23;

                a {
                    color: #e51c23;
                }
            }

            .modify {
                position: absolute;
                margin-left: 80px;
                margin-top: -10px;
                color: #3498db;

                a {
                    color: #3498db;
                }
            }
        }
    }
}
</style>


 
 * @Date: 2018-07-06 12:51:32 
 * @Last Modified by:   zhouyou@werun 
 * @Last Modified time: 2018-07-06 12:51:32 
 */

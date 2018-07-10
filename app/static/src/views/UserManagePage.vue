/*
 * @Author: zhouyou@werun 
 * @Descriptions: 用户管理界面 
 * @Date: 2018-07-06 09:31:58 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 10:15:01
 */

<template>
    <div id="user-manage-page">
        <div class="line">
            <h2>用户管理</h2>
        </div>
        <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/19.jpg" class="head-img">
                <span>大雄</span>
                <sapn class="lessor-role">出租用户</sapn>
                <br>
                <br>
                <span>联系电话：15550671537</span>
            </div>
            <div class="center-bar">
                <span>邮箱：zhouyou.world@outlook.com</span>
                <br>
                <br>
                <span>居住地址：哈尔滨工业大学威海</span>
            </div>
            <div class="right-bar">
                <span class="delete">
                    <i class="el-icon-circle-close"></i>&nbsp;删除账号</span>
                <br>
                <br>
                <span class="modify">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改密码</span>
            </div>
        </div>
        <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/20.jpg" class="head-img">
                <span>大雄</span>
                <sapn class="rent-role">租房用户</sapn>
                <br>
                <br>
                <span>联系电话：15550671537</span>
            </div>
            <div class="center-bar">
                <span>邮箱：zhouyou.world@outlook.com</span>
                <br>
                <br>
                <span>居住地址：哈尔滨工业大学威海</span>
            </div>
            <div class="right-bar">
                <span class="delete">
                    <i class="el-icon-circle-close"></i>&nbsp;删除账号</span>
                <br>
                <br>
                <span class="modify">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改密码</span>
            </div>
        </div>
        <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/21.jpg" class="head-img">
                <span>大雄</span>
                <sapn class="manager-role">平台管理员</sapn>
                <br>
                <br>
                <span>联系电话：15550671537</span>
            </div>
            <div class="center-bar">
                <span>邮箱：zhouyou.world@outlook.com</span>
                <br>
                <br>
                <span>居住地址：哈尔滨工业大学威海</span>
            </div>
            <div class="right-bar">
                <span class="delete">
                    <i class="el-icon-circle-close"></i>&nbsp;删除账号</span>
                <br>
                <br>
                <span class="modify">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改密码</span>
            </div>
        </div>

        <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/19.jpg" class="head-img">
                <span>大雄</span>
                <sapn class="system-manager-role">系统管理员</sapn>
                <br>
                <br>
                <span>联系电话：15550671537</span>
            </div>
            <div class="center-bar">
                <span>邮箱：zhouyou.world@outlook.com</span>
                <br>
                <br>
                <span>居住地址：哈尔滨工业大学威海</span>
            </div>
            <div class="right-bar">
                <span class="delete">
                    <i class="el-icon-circle-close"></i>&nbsp;删除账号</span>
                <br>
                <br>
                <span class="modify">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改密码</span>
            </div>
        </div>
    </div>

</template>


<script>
const UserManagePage = {};

export default UserManagePage;
</script>


<style lang="scss" scoped>
#user-manage-page {
    padding: 30px;
    text-align: left;

    .line {
        border-bottom: 1px solid #bbb;
    }

    .user {
        padding: 25px 0 25px;
        font-size: 14px;

        .left-bar {
            float: left;
            display: inline-block;
            width: 200px;
            padding-left: 90px;

            .head-img {
                position: absolute;
                margin-left: -75px;
                width: 60px;
                height: 60px;
                border-radius: 30px;
            }

            .lessor-role {
                margin-left: 10px;
                color: #ff5a5f;
                font-weight: bold;
            }

            .rent-role {
                margin-left: 10px;
                color: #259b24;
                font-weight: bold;
            }

            .manager-role {
                margin-left: 10px;
                color: #579fb2;
                font-weight: bold;
            }

            .system-manager-role {
                margin-left: 10px;
                color: #5a67ff;
                font-weight: bold;
            }
        }

        .center-bar {
            display: inline-block;
        }

        .right-bar {
            float: right;
            margin-right: 30px;

            .modify {
                color: #3498db;
            }

            .delete {
                color: #e51c23;
            }
        }
    }
}
</style>


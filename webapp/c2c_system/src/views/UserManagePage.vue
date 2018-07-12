/*
 * @Author: zhouyou@werun 
 * @Descriptions: 用户管理界面 
 * @Date: 2018-07-06 09:31:58 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 15:27:37
 */

<template>
    <div id="user-manage-page">
        <div class="line">
            <h2>用户管理</h2>
        </div>
        <div class="user line clearfix" v-for="(user, index) in userList" :key="index">
            <div class="left-bar">
                <img :src="returnHeadImg(user.headico)" class="head-img">
                <span>{{user.nickname}}</span>
                <span :class="{manager: user.role_id === 2,lessor: user.role_id === 3,rent: user.role_id === 4,}">{{user.role_name}}</span>
                <br>
                <br>
                <span>联系电话：{{user.phone}}</span>
            </div>
            <div class="center-bar">
                <span>邮箱：{{user.email}}</span>
                <br>
                <br>
                <span>姓名：{{user.name}}</span>
                <br>
                <br>
                <span>身份证号码：{{user.id_card}}</span>
            </div>
            <div class="right-bar">

                <el-button type="text" @click="changePassword(user.user_id)">
                    <i class="el-icon-edit-outline"></i>&nbsp;修改密码</el-button>
                <br>
                <br>
                <el-button class="setManager" type="text" @click="setManager(user.user_id, index)">
                    <i class="el-icon-edit-outline"></i>设置为平台管理员</el-button>
                <br>
                <br>
                <el-button class="delete" type="text" @click="deleteUser(user.user_id, index)">
                    <i class="el-icon-circle-close"></i>&nbsp;删除账号</el-button>
            </div>
        </div>
        <div class="load" @click="getUserList" v-show="!isEnd">
            加载更多
        </div>
        <!-- <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/19.jpg" class="head-img">
                <span>大雄</span>
                <span class="lessor-role">出租用户</span>
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
                <span class="rent-role">租房用户</span>
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
                <span class="manager-role">平台管理员</span>
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
        </div> -->

        <!-- <div class="user line clearfix">
            <div class="left-bar">
                <img src="../assets/19.jpg" class="head-img">
                <span>大雄</span>
                <span class="system-manager-role">系统管理员</span>
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
        </div> -->
    </div>

</template>


<script>
import { hex_md5 } from "../js/md5.js";
const defaultHeadImg = require("../assets/head-img.jpg");

const UserManagePage = {
    data: function() {
        return {
            userList: [],
            start: 0,
            isEnd: false
        };
    },
    methods: {
        getUserList: function() {
            const self = this;

            var postData = {
                index: this.start,
                count: 5
            };

            this.$axios
                .post("/c2c/userlist", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.userList = self.userList.concat(data.users);
                        self.start += 5;

                        if (data.empty) {
                            self.isEnd = true;
                        }
                    }
                });
        },

        returnHeadImg: function(img) {
            return img ? img : defaultHeadImg;
        },

        changePassword: function(userId) {
            const self = this;

            this.$prompt("请输入新的密码", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消"
            })
                .then(({ value }) => {
                    var postData = {
                        user_id: userId,
                        password: hex_md5(value)
                    };

                    this.$axios
                        .post("/c2c/system/userpasswordchange", postData)
                        .then(function(response) {
                            var data = response.data;

                            if (data.success) {
                                self.$message({
                                    message: "修改成功！",
                                    type: "success"
                                });
                            } else {
                                // update fail
                                self.$message.error("修改失败！");
                            }
                        });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "取消输入"
                    });
                });
        },

        setManager: function(userId, index) {
            const self = this;

            this.$confirm("确认将此用户设置为平台管理员吗?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "info"
            })
                .then(() => {
                    var postData = {
                        user_id: userId
                    };

                    this.$axios
                        .post("/c2c/rolechange", postData)
                        .then(function(response) {
                            var data = response.data;
                            if (data.success) {
                                self.userList[index].role_id = 2;
                                self.userList[index].role_name = "平台管理员";

                                self.$message({
                                    message: "设置成功！",
                                    type: "success"
                                });
                            } else {
                                self.$message.error("设置失败！");
                            }
                        });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消设置"
                    });
                });
        },

        deleteUser: function(userId, index) {
            const self = this;

            this.$confirm("确认删除此用户吗?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning"
            })
                .then(() => {
                    var postData = {
                        user_id: userId
                    };

                    this.$axios
                        .post("/c2c/userdel", postData)
                        .then(function(response) {
                            var data = response.data;
                            if (data.success) {
                                self.userList.splice(index, 1);
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
        }
    },
    created() {
        this.getUserList();
    }
};

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

            .lessor {
                margin-left: 10px;
                color: #ff5a5f;
                font-weight: bold;
            }

            .rent {
                margin-left: 10px;
                color: #259b24;
                font-weight: bold;
            }

            .manager {
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

            button {
                padding: 0;
            }

            .modify {
                color: #3498db;
            }

            .delete {
                color: #e51c23;
            }

            .setManager {
                color: #8bc34a;
            }
        }
    }

    .load {
        text-align: center;
        font-style: italic;
        font-size: 20.9984px;
        cursor: pointer;
        color: #c5c5c5;
    }
}
</style>


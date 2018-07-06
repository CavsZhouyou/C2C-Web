/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布旅游信息界面 
 * @Date: 2018-07-06 10:40:22 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 10:53:37
 */


<template>
    <div id="release-travel-information-page">
        <div class="line">
            <h2>发布旅游信息</h2>
        </div>
        <textarea v-model="conetnt" placeholder="请输入旅游信息" class="content"></textarea>
        <div class="button-container">
            <button class="common-button">点击发布</button>
        </div>
    </div>
</template>


<script>
const ReleaseDisclaimerPage = {};

export default ReleaseDisclaimerPage;
</script>

<style lang="scss" scoped>
#release-travel-information-page {
    padding: 30px;
    text-align: left;

    .line {
        border-bottom: 1px solid #bbb;
    }

    .content {
        margin-top: 20px;
        width: 100%;
        min-height: 550px;
        border: 1px solid #bbb;
    }

    .button-container {
        text-align: center;

        .common-button {
            margin-top: 35px;
            width: 150px;
            height: 40px;
        }
    }
}
</style>


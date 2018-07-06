/*
 * @Author: zhouyou@werun 
 * @Descriptions: 发布房源推荐信息页面
 * @Date: 2018-07-06 10:55:12 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 10:58:04
 */


<template>
    <div id="release-bujilding-recommend-page">
        <div class="line">
            <h2>发布房屋推荐信息</h2>
        </div>
        <textarea v-model="conetnt" placeholder="请输入房屋推荐信息" class="content"></textarea>
        <div class="button-container">
            <button class="common-button">点击发布</button>
        </div>
    </div>
</template>


<script>
const ReleaseBuildingRecommendPage = {};

export default ReleaseBuildingRecommendPage;
</script>

<style lang="scss" scoped>
#release-bujilding-recommend-page {
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
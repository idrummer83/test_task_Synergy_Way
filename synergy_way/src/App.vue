<template>
    <div class="container">

<!--        <ul class="nav nav-tabs nav-justified mt-5">-->
<!--            <li v-for="tab in tabs" :key="tab" @click="selected = tab;" class="nav-item">-->
<!--                <a class="nav-link active" href="#">{{ tab }}</a>-->
<!--            </li>-->
<!--        </ul>-->

<!--        <div class="tab-content py-3" id="">-->
<!--            <component :is="selected"></component>-->
<!--        </div>-->


        <b-card no-body class="mt-5">
            <b-tabs card>
                <b-tab v-for="i in tabs" :key="i" :title="'Tab ' + i">
                    <component :is="i"></component>
                </b-tab>
            </b-tabs>
        </b-card>

    </div>

</template>

<script type="text/javascript">

    import Groups from "./components/Groups.vue"
    import Users from "./components/Users.vue"

    export default {
        components: {Users, Groups,},
        data() {
            return {
                tabs: ['Users', 'Groups'],
                // tabbs: ["Users", "Groups"],
                // selected: "Users",
            }
        },
    }
</script>
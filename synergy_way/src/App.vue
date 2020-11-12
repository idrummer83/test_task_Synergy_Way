<template>
    <div class="container">

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
            }
        },
    }
</script>
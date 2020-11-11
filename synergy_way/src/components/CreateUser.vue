<template>
    <div>
        <h2>Create user</h2>

        <form v-on:submit.prevent="createUser()" enctype="multipart/form-data">
            <div class="form-group">
                <label for="username">Username</label>
                <input
                        type="text"
                        class="form-control"
                        id="username"
                        name="username"
                        placeholder="Enter username"
                        required="required"
                        v-model="username">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input
                            type="password"
                            class="form-control"
                            id="password"
                            name="password"
                            placeholder="Enter password"
                            required="required"
                            v-model="password">
                </div>

                <div class="form-group">
                    <label class="d-block" for="synergy_group">Select group</label>
                    <select name="synergy_group" id="synergy_group" class="custom-select"
                            v-model="selected">
                        <option disabled>Select group</option>
                        <option v-for="(item, idx) in group" v-bind:key="idx" v-bind:value="item.id">
                            {{item.title}}
                        </option>
                    </select>
                </div>

            <div>
                <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
        </form>

    </div>
</template>

<script>

    export default {
        name: "CreateUser",
        data() {
            return {
                'username': null,
                'password': null,
                'synergy_group': null,
                group: [],
                selected: '',
            }
        },
        created() {
            this.getGroups()
        },
        methods: {
            async createUser() {
                let data = {
                    'username': this.username,
                    'password': this.password,
                    'synergy_group': this.selected,
                }
                fetch(`${this.$store.getters.getServerUrl}/user_create/`,
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    this.clearForm()
                    return response
                    })
            },
            async getGroups(){
                this.group = await fetch(`${this.$store.getters.getServerUrl}/group_list/`,
                ).then(response => response.json())
            },
            clearForm() {
                this.username = ''
                this.password = ''
                this.selected = ''
            },
        },
    }

</script>

<style scoped>

</style>
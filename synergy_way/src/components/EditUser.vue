<template>
    <div>

        <h2>Edit user</h2>

        <form v-on:submit.prevent="editUser()">
            <div class="form-group">
                <label for="username">Username</label>
                <input
                        type="text"
                        class="form-control"
                        id="username"
                        name="username"
                        placeholder="Enter username"
                        required="required"
                        v-model="user.username">
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
                          v-model="user.password">
              </div>
              <div class="form-group">
                  <label class="d-block" for="synergy_group">Select group</label>
                  <select name="synergy_group" id="synergy_group" class="custom-select"
                          v-model="user.synergy_group">
                      <option disabled>Select group</option>
                      <option v-for="(item, idx) in group" v-bind:key="idx" v-bind:value="item.id">
                          {{item.title}}
                      </option>
                  </select>
              </div>

            <b-alert :show="alert" variant="success">User new edition saved.</b-alert>

            <div>
                <button type="submit" class="btn btn-primary" >Save changes</button>
            </div>
        </form>

    </div>
</template>

<script>
    export default {
        name: "EditUser",
        props: ['get_user_id'],
        data() {
            return {
                user: {},
                group: [],
                alert: false
            }
        },
        created() {
            this.loadUser()
            this.getGroups()
        },
        methods: {
            async loadUser() {
                this.user = await fetch(
                    `${this.$store.getters.getServerUrl}/user_edit/${this.get_user_id}`
                ).then(response => response.json())
            },
            async getGroups(){
                this.group = await fetch(`${this.$store.getters.getServerUrl}/group_list/`,
                ).then(response => response.json())
            },
            async editUser() {
                let data = {
                    'username': this.user.username,
                    'password': this.user.password,
                    'synergy_group': this.user.synergy_group
                }
                fetch(`${this.$store.getters.getServerUrl}/user_edit/${this.get_user_id}`,
                    {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    // this.clearForm()
                    this.alert = true
                    return response
                    })
            },
            clearForm() {
                this.user.username = ''
                this.user.password = ''
                this.user.synergy_group = ''
            }
        }
    }
</script>

<style scoped>

</style>
<template>
    <div>

          <b-modal id="modal-user" @hide="createActive(false), editActive(false), loadUsersList()">

              <CreateUser v-show="showcreate"/>
              <EditUser v-show="showedit" :get_user_id="user_id_edit" />

              <template v-slot:modal-footer="{ ok }">
                  <b-button size="sm" variant="success" @click="ok()">OK</b-button>
              </template>

          </b-modal>

        <div class="mb-5 mt-5">
            <b-button variant="btn btn-primary" v-on:click="createActive(true)" v-b-modal.modal-user>Create user</b-button>
        </div>
        <div class="row bg-light mb-3">
            <div class="col-1">User id</div>
            <div class="col-4">Usename</div>
            <div class="col-2">Date created</div>
            <div class="col-2">Group id</div>
            <div class="col-3">Action</div>
        </div>
        <div class="row mb-1" v-for="(user, idx) in users" :key="idx">
            <div class="col-1">{{ user.id }}</div>
            <div class="col-4">{{ user.username }}</div>
            <div class="col-2">{{ format(user.date_joined) }}</div>
            <div class="col-2">{{ user.synergy_group }}</div>
            <div class="col-3 d-flex justify-content-between">
                <b-button class="btn btn-info" v-b-modal.modal-user v-on:click="getUserId(user.id), editActive(true)">Edit user</b-button>
                <button class="btn btn-danger" v-on:click="deleteUser(user.id)">Delete user</button>
            </div>
        </div>
    </div>
</template>

<script>

    import moment from "moment";
    import CreateUser from './CreateUser'
    import EditUser from "./EditUser";

    export default {
        name: "Users",
        components: {CreateUser, EditUser},
        data() {
            return {
                users: [],
                showcreate: false,
                showedit: false,
                user_id_edit: ''
            }
        },
        created() {
            this.loadUsersList()
            this.getUserId()
        },
        methods: {
            createActive(val){
              if (val == true) {
                return this.showcreate = true
              } else {
                return this.showcreate = false
              }
            },
            editActive(val){
              if (val == true) {
                return this.showedit = true
              } else {
                return this.showedit = false
              }
            },
            format(value) {
                return moment(value).format('DD-MM-YYYY')
            },
            getUserId(item) {
              this.user_id_edit = item
            },
            async loadUsersList() {
                this.users = await fetch(
                    `${this.$store.getters.getServerUrl}/user_list/`
                ).then(response => response.json()
                )
            },
            async deleteUser(user_id) {
                let data = {
                    'user_id': user_id,
                }
                fetch(`${this.$store.getters.getServerUrl}/user_delete/`+ data.user_id,
                    {
                        method: 'DELETE',
                    }
                ).then(response => {
                        this.loadUsersList();
                        return response
                    })
            },
        }
    }
</script>

<style scoped>

</style>
<template>
    <div>

        <b-modal id="modal-group" @hide="createActive(false), editActive(false), loadGroupList()">

            <CreateGroup v-show="showcreate"/>
            <EditGroup v-show="showedit" :get_group_id="group_id_edit" />

            <template v-slot:modal-footer="{ ok }">
                <b-button size="sm" variant="success" @click="ok()">OK</b-button>
            </template>

        </b-modal>

        <div class="mb-5 mt-5">
            <b-button variant="btn btn-primary" v-on:click="createActive(true)" v-b-modal.modal-group>Create group</b-button>
        </div>

        <div class="row bg-light mb-3">
            <div class="col">id</div>
            <div class="col">title</div>
            <div class="col">action</div>
        </div>
        <div class="row mb-1" v-for="(item, idx) in groups" :key="idx">
            <div class="col">{{ item.id }}</div>
            <div class="col">{{ item.title }}</div>
            <div class="col d-flex justify-content-between">
                <b-button class="btn btn-info" v-b-modal.modal-group v-on:click="getGroupId(item.id), editActive(true)">Edit group</b-button>
                <button class="btn btn-danger" v-on:click="deleteGroup(item.id)">Delete group</button>
            </div>
        </div>

    </div>
</template>

<script>

    import CreateGroup from './CreateGroup';
    import EditGroup from "./EditGroup";

    export default {
        name: "Groups",
        components: {CreateGroup, EditGroup},
        data() {
            return {
                groups: [],
                showcreate: false,
                showedit: false,
                group_id_edit: '',
            }
        },
        created() {
            this.loadGroupList()
            this.getGroupId()
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
            getGroupId(item) {
                return this.group_id_edit = item
            },
            async loadGroupList() {
                this.groups = await fetch(
                    `${this.$store.getters.getServerUrl}/group_list/`
                ).then(response => response.json()
                )
            },
            async deleteGroup(group_id) {
                let data = {
                    'group_id': group_id,
                }
                fetch(`${this.$store.getters.getServerUrl}/group_delete/`+ data.group_id,
                    {
                        method: 'DELETE',
                    }
                ).then(response => {
                        this.loadGroupList();
                        return response
                    })
            },
        }
    }
</script>

<style scoped>

</style>
<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-12">
                <h2 class="mb-5 text-center mt-5">Test task synergy way</h2>

                <div class="vue_test">

                    <ul class="nav nav-tabs nav-justified">
                        <li class="nav-item">
                            <a class="nav-link" @click.prevent="setActive('users_list')"
                               :class="{ active: isActive('users_list') }" href="#users_list">Users</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click.prevent="setActive('groups')"
                               :class="{ active: isActive('groups') }" href="#groups">Groups</a>
                        </li>

                    </ul>
                    <div class="tab-content py-3" id="myTabContent">
                        <div class="tab-pane fade" :class="{ 'active show': isActive('users_list') }" id="home">

                            <div class="mb-5">
                                <button class="btn btn-primary" v-on:click="addUser()">Create user</button>
                            </div>

                            <div class="row bg-secondary mb-3">
                                <div class="col-1">id</div>
                                <div class="col-2">usename</div>
                                <div class="col">date created</div>
                                <div class="col-2">group id</div>
                                <div class="col-2">action</div>
                            </div>
                            <div class="row" v-for="user in users" :key="user">
                                <div class="col-1">{{ user.id }}</div>
                                <div class="col-2">{{ user.username }}</div>
                                <div class="col">{{ format(user.date_joined) }}</div>
                                <div class="col-2">{{ user.synergy_group }}</div>
                                <div class="col-2">
                                    <button class="btn btn-info" v-on:click="getUser(user.id)">Edit</button>
                                    <button class="btn btn-danger" v-on:click="deleteUser(user.id)">delete</button>
                                </div>
                            </div>

                        </div>

                        <div class="tab-pane fade" :class="{ 'active show': isActive('groups') }" id="profile">

                            <button type="button" v-on:click="addGroup()" class="btn btn-primary mb-5">Create group
                            </button>

                            <div class="row bg-secondary mb-3">
                                <div class="col">id</div>
                                <div class="col">title</div>
                                <div class="col">action</div>
                            </div>
                            <div class="row" v-for="item in group" :key="item">
                                <div class="col">{{ item.id }}</div>
                                <div class="col">{{ item.title }}</div>
                                <div class="col">
                                    <button class="btn btn-info" v-on:click="getGroup(item.id)">Edit</button>
                                    <button class="btn btn-danger" v-on:click="deleteGroup(item.id)">Delete</button>
                                </div>
                            </div>

                        </div>

                    </div>

                    <!-- Edit Group Modal -->
                    <div class="" id="editGroupModal" v-if="showModalEdit" tabindex="-1" role="dialog">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLongTitle">EDIT GROUP</h5>
                                    <button type="button" @click="showModalEdit=false" class="close"
                                            data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <form v-on:submit.prevent="editGroup()">
                                    <div class="modal-body">
                                        <div class="form-group">
                                            <label for="title">Group Heading</label>
                                            <input
                                                    type="text"
                                                    class="form-control"
                                                    id="titl1e"
                                                    name="title"
                                                    placeholder="Enter group title"
                                                    required="required"
                                                    v-model="currentGroup.title">
                                        </div>
                                        <div class="form-group">
                                            <label for="description">Group Body</label>
                                            <textarea
                                                    class="form-control"
                                                    id="description1"
                                                    name="description"
                                                    placeholder="Enter Group Body"
                                                    required="required"
                                                    v-model="currentGroup.description"
                                                    rows="3"></textarea>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" @click="showModalEdit=false"
                                                class="btn btn-secondary m-progress" data-dismiss="modal">Close
                                        </button>
                                        <button type="submit" class="btn btn-primary">Save changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <!-- End of edit group modal -->

                    <!-- Add Group Modal -->
                    <div class=" " id="addGroupModal" v-if="showModalGroup" tabindex="-1" role="dialog"
                         aria-labelledby="exampleModalLongTitle" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLongTitle1">ADD group</h5>
                                    <button @click="showModalGroup=false" type="button" class="close"
                                            data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <form v-on:submit.prevent="addGroup()">
                                    <div class="modal-body">
                                        <div class="form-group">
                                            <label for="title">group Heading</label>
                                            <input
                                                    type="text"
                                                    class="form-control"
                                                    id="title"
                                                    name="title"
                                                    placeholder="Enter group title"
                                                    required="required"
                                                    v-model="newGroup.title"
                                            >
                                        </div>
                                        <div class="form-group">
                                            <label for="description">group description</label>
                                            <textarea
                                                    class="form-control"
                                                    id="description"
                                                    name="description"
                                                    placeholder="Enter Group Body"
                                                    rows="3"
                                                    required="required"
                                                    v-model="newGroup.description"
                                            ></textarea>

                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" @click="showModalGroup=false"
                                                data-dismiss="modal">Close
                                        </button>
                                        <button type="submit" class="btn btn-primary">Save changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <!--<div class="loading" v-if="loading===true">Loading&#8230;</div>-->
                    </div>
                    <!-- End of group modal -->

                    <!-- Add User Modal -->
                    <div class=" " id="addUserModal" v-if="showModalUser" tabindex="-1" role="dialog">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLongTitle12">Add user</h5>
                                    <button @click="showModalUser=false" type="button" class="close"
                                            data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <form v-on:submit.prevent="addUser()">
                                    <div class="modal-body">
                                        <div class="form-group">
                                            <label for="title">Username</label>
                                            <input
                                                    type="text"
                                                    class="form-control"
                                                    id="username"
                                                    name="username"
                                                    placeholder="Enter username"
                                                    required="required"
                                                    v-model="newUser.username">
                                        </div>
                                        <div class="form-group">
                                            <label for="title">Password</label>
                                            <input
                                                    type="password"
                                                    class="form-control"
                                                    id="password"
                                                    name="password"
                                                    placeholder="Enter password"
                                                    required="required"
                                                    v-model="newUser.password">
                                        </div>
                                        <div class="form-group">
                                            <label for="synergy_group">Select group</label>
                                            <select name="synergy_group" id="synergy_group"
                                                    v-model="newUser.synergy_group" @change="onChange(this.value)">
                                                <option></option>
                                                <option :value="item.id" v-for="item in group" :key="item">
                                                    {{item.title}}
                                                </option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" @click="showModalUser=false"
                                                data-dismiss="modal">Close
                                        </button>
                                        <button type="submit" class="btn btn-primary">Save changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <!--<div class="loading" v-if="loading===true">Loading&#8230;</div>-->
                    </div>
                    <!-- End of user modal -->

                    <!-- Edit User Modal -->
                    <div class=" " id="editUserModal" v-if="showModalUserEdit" tabindex="-1" role="dialog">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLongTitle112">Edit user</h5>
                                    <button @click="showModalUserEdit=false" type="button" class="close"
                                            data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <form v-on:submit.prevent="editUser()">
                                    <div class="modal-body">
                                        <div class="form-group">
                                            <label for="title">Username</label>
                                            <input
                                                    type="text"
                                                    class="form-control"
                                                    id="username1"
                                                    name="username"
                                                    placeholder="Enter username"
                                                    required="required"
                                                    v-model="currentUser.username">
                                        </div>
                                        <div class="form-group">
                                            <label for="title">Password</label>
                                            <input
                                                    type="password"
                                                    class="form-control"
                                                    id="password1"
                                                    name="password"
                                                    placeholder="Enter password"
                                                    required="required"
                                                    v-model="currentUser.password">
                                        </div>
                                        <div class="form-group">
                                            <label for="synergy_group">Select group</label>
                                            <select name="synergy_group" id="synergy_group1"
                                                    v-model="currentUser.synergy_group" @change="onChange(this.value)">
                                                <option></option>
                                                <option :value="item.id" v-for="item in group" :key="item">
                                                    {{item.title}}
                                                </option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" @click="showModalUserEdit=false"
                                                data-dismiss="modal">Close
                                        </button>
                                        <button type="submit" class="btn btn-primary">Save changes</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <!-- End of user modal -->

                </div>

                <!--<router-view />-->
            </div>
        </div>
    </div>

</template>

<script type="text/javascript">
    import axios from 'axios';
    import moment from 'moment'

    export default {
        data() {
            return {
                activeItem: 'users_list',
                group: null,
                users: null,
                newGroup: {'title': null, 'description': null},
                currentGroup: {},
                newUser: {'username': null, 'password': null, 'synergy_group': null},
                currentUser: {},
                showModalGroup: false,
                showModalEdit: false,
                showModalUser: false,
                showModalUserEdit: false
            }
        },
        mounted() {
            axios.get('http://127.0.0.1:8000/group_list/')
                .then(response => {
                    console.log('data', response.data);
                    this.group = response.data
                });
            axios.get('http://127.0.0.1:8000/user_list/')
                .then(response => {
                    console.log('data', response.data);
                    this.users = response.data
                });
        },
        methods: {
            format(value) {
                return moment(value).format('DD-MM-YYYY')
            },
            isActive(menuItem) {
                return this.activeItem === menuItem
            },
            setActive(menuItem) {
                this.activeItem = menuItem
            },

            editGroup: function () {
                this.loading = true;
                axios.put('http://127.0.0.1:8000/group_edit/' + this.currentGroup.id, this.currentGroup)
                    .then((response) => {
                        this.loading = false;
                        this.currentGroup = response.data;
                        this.getAllGroups();
                        this.showModalEdit = false;
                        return response
                    })
                    .catch((err) => {
                        this.loading = false;
                        console.log(err);
                    })
            },
            editUser: function () {
                this.loading = true;
                axios.put('http://127.0.0.1:8000/user_edit/' + this.currentUser.id, this.currentUser)
                    .then((response) => {
                        this.loading = false;
                        this.currentUser = response.data;
                        this.getAllUsers();
                        this.showModalUserEdit = false;
                        return response
                    })
                    .catch((err) => {
                        this.loading = false;
                        console.log(err);
                    })
            },
            getGroup: function (id) {
                this.showModalEdit = true;
                axios.get('http://127.0.0.1:8000/group_edit/' + id)
                    .then((response) => {
                        this.currentGroup = response.data;
                        this.loading = false;
                        return response;
                    })
            },
            getUser: function (id) {
                this.showModalUserEdit = true;
                axios.get('http://127.0.0.1:8000/user_edit/' + id)
                    .then((response) => {
                        this.currentUser = response.data;
                        this.loading = false;
                        return response;
                    })
            },
            getAllGroups: function () {
                this.loading = true;
                axios.get('http://127.0.0.1:8000/group_list/')
                    .then((response) => {
                        this.group = response.data;
                        this.loading = false;
                    })
                    .catch((err) => {
                        this.loading = false;
                        console.log(err);
                    })
            },
            getAllUsers: function () {
                this.loading = true;
                axios.get('http://127.0.0.1:8000/user_list/')
                    .then((response) => {
                        this.users = response.data;
                        this.loading = false;
                    })
                    .catch((err) => {
                        this.loading = false;
                        console.log(err);
                    })
            },
            addGroup: function () {
                this.showModalGroup = true;
                this.loading = true;
                axios.post('http://127.0.0.1:8000/group_create/', this.newGroup, {
                    headers: {
                        'Accept': 'application/json',
                        // 'Content-Type': 'application/vnd.api+json'
                        //   'Content-Type': 'application/x-www-form-urlencoded'
                        'Content-Type': 'application/json'
                    }
                })
                    .then((response) => {
                        this.loading = false;
                        this.getAllGroups();
                        this.showModalGroup = false;
                        return response
                    })
            },
            addUser: function () {
                this.showModalUser = true;
                this.loading = true;
                axios.post('http://127.0.0.1:8000/user_create/', this.newUser, {
                    headers: {
                        'Accept': 'application/json',
                        // 'Content-Type': 'application/vnd.api+json'
                        //   'Content-Type': 'application/x-www-form-urlencoded'
                        'Content-Type': 'application/json'
                    }
                })
                    .then((response) => {
                        console.log(this.newUser);
                        this.loading = false;
                        this.getAllUsers();
                        this.showModalUser = false;
                        return response
                    })
            },
            deleteGroup: function (id) {
                axios.delete('http://127.0.0.1:8000/group_delete/' + id)
                    .then(response => {
                        this.loading = true;
                        this.getAllGroups();
                        return response
                    })
                    .catch((err) => {
                        this.loading = false;
                        alert('User in group. If you want to delete group, delete user from group at first.', err);
                    })
            },
            deleteUser: function (id) {
                axios.delete('http://127.0.0.1:8000/user_delete/' + id)
                    .then(response => {
                        this.loading = true;
                        this.getAllUsers();
                        return response
                    })
                    .catch((err) => {
                        this.loading = false;
                        console.log(err);
                    })
            },
        }
    }
</script>
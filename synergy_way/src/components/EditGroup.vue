<template>
    <div>
        <h2>Edit group</h2>

        <form v-on:submit.prevent="editGroup()">
            <div class="form-group">
                <label for="title">Group title</label>
                <input
                        type="text"
                        class="form-control"
                        id="title"
                        name="title"
                        placeholder="Enter group title"
                        required="required"
                        v-model="group.title">
            </div>
            <div class="form-group">
                <label for="description">Group description</label>
                <textarea
                        class="form-control"
                        id="description"
                        name="description"
                        placeholder="Enter group description"
                        required="required"
                        v-model="group.description"
                        rows="3"></textarea>
            </div>

            <b-alert :show="alert" variant="success">Group new edition saved.</b-alert>

            <div>
                <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "EditGroup",
        props: ['get_group_id'],
        data() {
            return {
                group: {},
                alert: false
            }
        },
        created() {
            this.loadGroup()
        },
        methods: {
            async loadGroup() {
                this.group = await fetch(
                    `${this.$store.getters.getServerUrl}/group_edit/${this.get_group_id}`
                ).then(response => response.json())
            },
            async editGroup() {
                let data = {
                    'title': this.group.title,
                    'description': this.group.description,
                }
                fetch(`${this.$store.getters.getServerUrl}/group_edit/${this.get_group_id}`,
                    {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json',
                        },
                        body: JSON.stringify(data)
                    }
                ).then(response => {
                    this.alert = true
                    return response
                    })
            },
            clearForm() {
                this.group.title = ''
                this.group.description = ''
            }
        }
    }
</script>

<style scoped>

</style>
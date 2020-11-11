<template>
    <div>
        <h2>Create group</h2>

        <form v-on:submit.prevent="createGroup()">
            <div class="form-group">
                <label for="title">Group title</label>
                <input
                        type="text"
                        class="form-control"
                        id="title"
                        name="title"
                        placeholder="Enter group title"
                        required="required"
                        v-model="title"
                >
            </div>
            <div class="form-group">
                <label for="description">Group description</label>
                <textarea
                        class="form-control"
                        id="description"
                        name="description"
                        placeholder="Enter Group Body"
                        rows="3"
                        required="required"
                        v-model="description"
                ></textarea>

            </div>

            <div>
                <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
        </form>
    </div>
</template>

<script>
    export default {
        name: "CreateGroup",
        data() {
            return {
                'title': null,
                'description': null,
            }
        },
        methods: {
            async createGroup() {
                let data = {
                    'title': this.title,
                    'description': this.description,
                }
                fetch(`${this.$store.getters.getServerUrl}/group_create/`,
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
            clearForm() {
                this.title = ''
                this.description = ''
            },
        }
    }
</script>

<style scoped>

</style>
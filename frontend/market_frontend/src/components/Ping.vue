<script>
    import axios from 'axios';


    const number = 10;

    export default {
        name : 'Ping',
        data() {
            return {
                users : '',
                kek : number
            };
        },
        methods: {
            getMessage() {
                const path = 'http://127.0.0.1:8000/get_user_by_id?id_=3';
                axios.get(path)
                    .then((res) => {
                        console.log(res.data);
                        
                        this.users = res.data; 
                    })
                    .catch((error) => {
                        console.log(error)
                    });
            },
        },
        created() {
            this.getMessage();
        },
    };

</script>


<template>
    <div class="container">
        <p v-for="user in users">
            {{ user.name }} {{ user.surname }} {{ user.email }} {{ user.city }} 
            <br>
            items: <br><p v-for="item in user.items">{{ item.title }}</p>
        </p>
    </div>
</template>
<template>
    <div>
        <h3>The new value is: {{ car_name }}</h3>
        <div>
            <label for="change">To replace a value please enter existing id here:</label><p></p>
            <input class="form-control" v-model="car_id">
            <label for="name">Car name:</label><p></p>
            <input class="form-control" v-model="car_name">
            <label for="coupe">Is it a coupe?:</label><p></p>
            <input class="form-control" v-model="coupe">
            <label for="topSpeed">Top Speed:</label><p></p>
            <input class="form-control" v-model="top_speed">
            <label for="dateOfPurchase">Date of Purchase:</label><p></p>
            <input class="form-control" v-model="date_of_purchase">
            <button class="btn btn-outline-danger m-3" @click="updateNewCars(car_id,car_name,coupe,top_speed,date_of_purchase)" style="width: 5rem;">Update</button>
            <button class="btn btn-outline-danger m-3" @click="saveNewCars(car_name,coupe,top_speed,date_of_purchase)" style="width: 5rem;">Submit</button>
        </div>
    </div>

</template>


<script>
    export default{
        data(){
            return  {
                car_id:"",
                car_name:"", 
                coupe:"",
                top_speed:"",
                date_of_purchase:""

            }
        },
        methods:{
            async saveNewCars(car_name,coupe,top_speed,date_of_purchase){
                const object={car_name, coupe, top_speed, date_of_purchase};
                const response = await fetch("http://localhost:8000/api/cars/", {
                    method: 'POST',
                    body: JSON.stringify(object)
                })
                
                if(respone.ok){
                    console.log(object)
                    let data = await response.json();
                    // this
                }

            },

            async updateNewCars(car_id,car_name,coupe,top_speed,date_of_purchase){
                const object={car_id,car_name, coupe, top_speed, date_of_purchase};
                const response = await fetch("http://localhost:8000/api/cars/", {method: 'PUT',
                body: JSON.stringify(object)})
                
                console.log(object)
                return response.json();
            }
        }
    
}
</script>
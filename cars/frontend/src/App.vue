<template>

  <div class="p-3 mb-2 bg-dark text-white main">
    <h1>My cars</h1>
    <button class="btn btn-outline-light" @click="fetch_cars">Fetch Cars</button>
    <p></p>
    <div>
      <ol style="padding-right: 32px;">
        <li style="width: 20rem;" v-for="car in cars">
          <p></p>
          (ID: {{ car.car_id }})
          <p></p>
          (Model: {{ car.car_name }})
          <p></p>
          (Coupe:{{ car.coupe }})
          <p></p>
          (Top speed: {{ car.top_speed }})
          <p></p>
          (Date of purchase: {{ car.date_of_purchase }})
          <p></p>
          <button class="btn btn-outline-danger m-3" @click="delete_cars(car.car_id)"
            style="width: 5rem;">Delete</button>
          <p></p>
          <HR>
          </HR>
        </li>
      </ol>
      <!-- <h4 v-else>There are no cars to display.</h4>   -->
    </div>

  </div>
  <!-- <Mycompenent class="form"></Mycompenent> -->
  <div class="form">
    <!-- <h3>The new value is: {{ car_name }}</h3> -->
    <div>
      <label for="change">To replace a value please enter existing ID here:</label>
      <p></p>
      <input type="number" class="form-control" name="car_id" v-model="car_id">
      <label for="name">Car name:</label>
      <p></p>
      <input class="form-control" name="car_name" v-model="car_name">
      <label for="coupe">Is it a coupe?:</label>
      <p></p>
      <input type="checkbox" class="" name="coupe" v-model="coupe">
      <p></p>
      <label for="topSpeed">Top Speed:</label>
      <p></p>
      <input type="number" class="form-control" name="top_speed" v-model="top_speed">
      <label for="date_of_purchase">Date of Purchase:</label>
      <p></p>
      <input type="date" class="form-control" name="date_of_purchase" v-model="date_of_purchase">
      <button class="btn btn-outline-warning m-3"
        @click="update_new_cars(car_id, car_name, coupe, top_speed, date_of_purchase)"
        style="width: 5rem;">Update</button>
      <button class="btn btn-outline-success m-3" @click="save_new_cars(car_name, coupe, top_speed, date_of_purchase)"
        style="width: 5rem;">Submit</button>
    </div>
  </div>
</template>

<script>
import { objectToString } from '@vue/shared';
import Mycompenent from './components/MyCompenent.vue'

export default {
  components: {
    Mycompenent,
  },
  data() {
    return {
      cars: [],
    };
  },
  methods: {
    async fetch_cars() {
      let response = await fetch("http://localhost:8000/cars/api/cars/");
      let data = await response.json();
      this.cars = data.cars;

    },

    async delete_cars(car_id) {
      console.log(car_id)
      await fetch('http://localhost:8000/cars/api/cars1/' + car_id + "/", { method: 'DELETE' });
      this.fetch_cars()
    },

    async save_new_cars(car_name, coupe, top_speed, date_of_purchase) {
      const object = { car_name: car_name, coupe: coupe, top_speed: top_speed, date_of_purchase: date_of_purchase };
      const response = await fetch("http://localhost:8000/cars/api/cars/", {
        method: 'POST',
        body: JSON.stringify(object)

      })
      console.log(object)
      if (response.ok) {
        console.log(object)
        let data = await response.json();
        this.cars = data.cars
      }
      this.fetch_cars()
    },

    async update_new_cars(car_id, car_name, coupe, top_speed, date_of_purchase) {
      const object = {
        car_id: car_id, car_name: car_name, coupe: coupe, top_speed: top_speed, date_of_purchase: date_of_purchase
      };
      const response = await fetch('http://localhost:8000/cars/api/cars2/' + car_id + "/", {
        method: 'PUT',
        body: JSON.stringify(object)
      })

      console.log(object)
      if (response.ok) {
        console.log(object)
        let data = await response.json();
        this.cars = data.cars
      }
      this.fetch_cars()
    }


  },
  mounted() {
    this.fetch_cars()
  },

  components: { Mycompenent }
}
</script>




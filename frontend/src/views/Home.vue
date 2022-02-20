<template>
  <div class="home">
    <global-header/>
    <main class="container mt-5 p-5">
      <p class="h5 mb-5">Today's your FORTUNE</p>
      <b-card>
        <b-form @submit.prevent="submitInfo">
          <div class="row form-group">
            <label class="col-sm-3 col-form-label">birth date</label>
            <b-input-group class="col-sm-8">
              <b-form-input
                v-model="form.birth_date"
                type="text"
                placeholder="ex) 1999-10-17"
                required
              ></b-form-input>
              <b-input-group-append>
                <b-form-datepicker
                  v-model="form.birth_date"
                  button-only
                  initial-date="2000-01-01"
                  right
                  locale="en-US"
                ></b-form-datepicker>
              </b-input-group-append>
            </b-input-group>
          </div>
          <div class="row form-group">
            <label class="col-sm-3 col-form-label">blood type</label>
            <div class="col-sm-8">
              <b-form-select
                class="form-control"
                v-model="form.blood_type" :options="form.options"
                required
              />
            </div>
          </div>
          <div class="row test-center mt-5">
            <div class="col-sm-12">
              <b-button type="submit" variant="primary">
                submit
              </b-button>
            </div>
          </div>
        </b-form>
      </b-card>
      <div class="mt-5">
        <b-card title="Result">
          <b-card-text>
           today: {{ current_date }}
          </b-card-text>
          <b-card-text class="h5">
            Fortune Level: {{ fortune_with_star }} {{ fortune }}
          </b-card-text>
          <b-card-text>
            (Ranges from {{ fortune_range[0] }} to {{ fortune_range[1] }}.)
          </b-card-text>
        </b-card>
      </div>
    </main>
  </div>
</template>

<script>
import GlobalHeader from '../components/GlobalHeader.vue';
import api from "../services/api"

export default {
  name: "Home",
  components: {
    GlobalHeader,
  },
  data() {
    return {
      form: {
        birth_date: null,
        blood_type: null,
        options: [
          { value: null, text: 'Please select an option.' },
          { value: 'A', 'text': 'A'},
          { value: 'B', 'text': 'B'},
          { value: 'O', 'text': 'O'},
          { value: 'AB', 'text': 'AB'},
        ]
      },
      current_date: null,
      fortune_range: [],
      fortune: null,
    };
  },
  computed: {
    fortune_with_star: function () {
      let stars = "";
        for (let index = this.fortune_range[0]; index <= this.fortune_range[1]; index++) {
          if (index <= this.fortune) {
            stars += "★"              
          } else {
            stars += "☆"
          }
        }
      return stars;
    },
  },
  methods: {
    submitInfo: function () {
      api({
        method: "post",
        url: "",
        data: {
          birth_date: this.form.birth_date,
          blood_type: this.form.blood_type,
        },
      })
      .then(response => {
        const resp_data = response.data
        this.current_date = resp_data.current_date;
        this.fortune = resp_data.fortune;
        this.fortune_range = resp_data.fortune_range;
      });
    },
  },
};
</script>

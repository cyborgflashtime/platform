<template>
  <div class="wrapper">
    <div class="content">
      <div class="block1 wd12" id="block1">
        <h1>Activation</h1>
        <div class="row-no-gutters settingsblock">

          <div class="col2">
            <div class="setline">
              <span class="span">Activated to: </span><a id="txt_device_domain" :href="url">{{ url }}</a>
            </div>

            <div class="setline">
              <span class="span">You can assign different<br>domain name to your device</span>
              <div class="spandiv">
                <button class="buttonblue bwidth smbutton" id="btn_reactivate" @click="reactivate">Reactivate</button>
              </div>
            </div>

          </div>

        </div>
      </div>
    </div>
  </div>

  <Error ref="error"/>

</template>

<script>
import axios from 'axios'
import Error from '@/components/Error'
import 'bootstrap'
import 'bootstrap-switch'

export default {
  name: 'Activation',
  props: {
    onLogin: Function,
    onLogout: Function
  },
  data () {
    return {
      url: 'Loading ...'
    }
  },
  components: {
    Error
  },
  mounted () {
    axios
      .get('/rest/settings/device_url')
      .then(resp => {
        this.url = resp.data.device_url
      })
      .catch(err => {
        this.$refs.error.showAxios(err)
      })
  },
  methods: {
    reactivate: function () {
      axios
        .post('/rest/settings/deactivate')
        .then(_ => {
          this.$router.push('/activate')
        })
        .catch(err => {
          this.$refs.error.showAxios(err)
        })
    }
  }
}
</script>
<style>
@import '../style/site.css';
@import '../style/material-icons.css';
</style>

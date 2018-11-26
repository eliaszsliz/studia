import colors from 'vuetify/es5/util/colors';

const { VUE_APP_SERVER_IP, VUE_APP_API_PORT } = process.env;

const HOSTNAME = `http://${VUE_APP_SERVER_IP}:${VUE_APP_API_PORT}`;
const ROOT_API = `http://${VUE_APP_SERVER_IP}:${VUE_APP_API_PORT}`;

const THEME_SETTINGS = {
  primary: '#005A7B',
  secondary: colors.grey.darken3,
  accent: '#582c39',
  error: '#FF5252',
  info: '#2196F3',
  success: '#4CAF50',
  warning: '#FFC107',
  primary_light: '#e6edfa',
  primary_light_2: '#f1f4fb',
};

const CSS_SETTINGS = {
  normalElevationClasses: 'elevation-0',
  activeElevationClasses: 'elevation-10',
  mobileBreakPoint: 1264,
  sidebarWidth: 300,
};


export { HOSTNAME, ROOT_API, CSS_SETTINGS, THEME_SETTINGS };


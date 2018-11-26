module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/airbnb'
  ],
  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
    'no-param-reassign': 0,
    'no-mixed-operators': 0,
    'vue/attribute-hyphenation': [
      'error',
      'always'
    ],
    'vue/require-prop-types': 'error',
    'vue/attributes-order': 'error',
    'vue/order-in-components': 'error'
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
}
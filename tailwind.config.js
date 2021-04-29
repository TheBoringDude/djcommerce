const colors = require("tailwindcss/colors")

module.exports = {
  purge: ['./**/*.html'],
  darkMode: false, // or 'media' or 'class'
  mode: 'jit',
  theme: {
    colors: colors,
    fontFamily: {
      sans: ['"Rubik"', "sans-serif"],
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
};

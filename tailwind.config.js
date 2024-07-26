/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/**/*.js"],
  theme: {
    fontFamily: {
      'Inter': ['Inter'],
      'Prata': ['Prata'],
      'Roboto': ['Roboto']
      },
    extend: {
      keyframes: {
        "open-menu": {
          "0%": { transform: "scaleY(0)" },
          "80%": { transform: "scaleY(1.2)" },
          "100%": { transform: "scaleY(1)" },
        },
        "marquee":{
        
          "100%": {transform: 'translate(-100%)'},
        }
      },
      animation: {
        "open-menu": "open-menu 0.5s ease-in-out forwards",
      },
      animation: {
        'marquee': 'marquee var(--marquee-duration) linear infinite',
        
      },
    },
  },
  plugins: [],
}


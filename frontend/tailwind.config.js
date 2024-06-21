/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          500: "#EC194C",
          700: "#C71B45",
          800: "#A91D3F",
          300: "#F64872",
        },
        secondary: "#C3CAD9",
        dark: "#333436",
      },
    },
  },
  plugins: [],
};

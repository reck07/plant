import type { Config } from "tailwindcss"

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#2d6a4f",
        secondary: "#40916c",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}

export default config
import logo from "../assets/logos/Logo.svg";
import { Button } from "@mui/material";

export const Footer = () => {
  return (
    <footer className="h-24 bg-[#2b2b2b] flex items-center justify-between px-10">
      <img src={logo} alt="worldforge" className="w-64" />
      <div className="flex gap-3">
        <Button
          variant="contained"
          sx={{
            bgcolor: "var(--color-orange-500)",
            fontWeight: "bold",
            fontSize: "16px",
            width: "fit-content",
            padding: "10px",
            transition: "all 0.3s ease",
            "&:hover": {
              bgcolor: "var(--color-orange-700)",
            },
          }}
        >
          Login
        </Button>
        <Button
          variant="contained"
          sx={{
            bgcolor: "var(--color-orange-500)",
            fontWeight: "bold",
            fontSize: "16px",
            width: "fit-content",
            padding: "10px",
            transition: "all 0.3s ease",
            "&:hover": {
              bgcolor: "var(--color-orange-700)",
            },
          }}
        >
          Create Account
        </Button>
      </div>
    </footer>
  );
};

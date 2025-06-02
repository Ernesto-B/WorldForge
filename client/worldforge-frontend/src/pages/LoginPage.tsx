import { Button, TextField, Typography, Link } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { login } from "../auth/authService";
import { useState } from "react";

export const LoginPage = () => {
  const nav = useNavigate();

  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    nav("/hub");
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Successfully logged in");
  };

  return (
    <main className="min-h-dvh bg-[#1b1b1b] flex justify-center items-center bg-[url(/src/assets/images/bg5.jpeg)] bg-cover bg-no-repeat">
      <form
        className="w-[350px] bg-[#2b2b2b] border-2 border-[#ffa500] flex flex-col gap-4 p-8 rounded-lg text-[#f0f0f0]"
        onSubmit={handleSubmit}
      >
        <Typography
          variant="h1"
          fontSize={30}
          fontWeight="bold"
          color="#ffa500"
        >
          LOGIN
        </Typography>
        <TextField
          label="Email"
          value={email}
          type="email"
          required
          fullWidth
          onChange={(e) => setEmail(e.target.value)}
          InputLabelProps={{
            style: { color: "#ffa500" },
          }}
          InputProps={{
            style: { color: "#fff" },
          }}
          sx={{
            "& .MuiOutlinedInput-root": {
              "& fieldset": { borderColor: "#ffa500" },
              "&:hover fieldset": { borderColor: "#ffa500" },
              "&.Mui-focused fieldset": { borderColor: "#ffa500" },
            },
            "& .MuiFormHelperText-root": { color: "#f87171" }, // optional: error text color
          }}
        />
        <TextField
          required
          label="Password"
          value={password}
          type="password"
          fullWidth
          onChange={(e) => setPassword(e.target.value)}
          InputLabelProps={{
            style: { color: "#ffa500" },
          }}
          InputProps={{
            style: { color: "#fff" },
          }}
          sx={{
            "& .MuiOutlinedInput-root": {
              "& fieldset": { borderColor: "#ffa500" },
              "&:hover fieldset": { borderColor: "#ffa500" },
              "&.Mui-focused fieldset": { borderColor: "#ffa500" },
            },
            "& .MuiFormHelperText-root": { color: "#f87171" },
          }}
        />
        <Button
          type="submit"
          variant="contained"
          sx={{
            bgcolor: "var(--color-orange-500)",
            fontWeight: "bold",
            fontSize: "16px",
            padding: "10px",
            transition: "all 0.3s ease",
            "&:hover": {
              bgcolor: "var(--color-orange-700)",
            },
          }}
        >
          Enter WorldForge
        </Button>
        <Link href="/register" color="#ffa500" width="fit-content">
          Register here.
        </Link>
      </form>
    </main>
  );
};

import { Button, Link, TextField, Typography } from "@mui/material";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../auth/authService";

export const RegisterPage = () => {
  const nav = useNavigate();

  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const data = await register(email, password);
      console.log("Registration successful:", data);
    } catch (error: any) {
      console.error(
        "Registration failed:",
        error.response?.data || error.message
      );
    }
  };

  return (
    <main className="min-h-dvh bg-[#1b1b1b] flex justify-center items-center bg-[url(/src/assets/images/bg5.jpeg)] bg-cover bg-no-repeat">
      <form
        className="w-[350px] bg-[#2b2b2b] border-2 border-[#ffa500] flex flex-col gap-4 p-8 rounded-lg text-[#f0f0f0]"
        onSubmit={handleSubmit}
      >
        <Typography
          variant="h1"
          fontSize={28}
          fontWeight="bold"
          color="#ffa500"
        >
          REGISTER
        </Typography>
        <TextField
          required
          label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          fullWidth
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
          label="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          fullWidth
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
          Create Account
        </Button>
        <Link href="/login" color="#ffa500" width="fit-content">
          Login here.
        </Link>
      </form>
    </main>
  );
};

import { Box, Button, TextField, Typography, Link } from "@mui/material";
import { useForm, SubmitHandler } from "react-hook-form";
import { useNavigate } from "react-router-dom";

interface LoginFormInputs {
  email: string;
  password: string;
}

export const LoginPage = () => {
  const nav = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormInputs>({ mode: "onSubmit" });

  const onSubmit: SubmitHandler<LoginFormInputs> = (data) => {
    console.log("Login data:", data);
    nav("/");
  };

  return (
    <main className="min-h-dvh bg-[#1b1b1b] flex justify-center items-center bg-[url(/src/assets/images/bg5.jpeg)] bg-cover bg-no-repeat">
      <Box
        component="form"
        onSubmit={handleSubmit(onSubmit)}
        sx={{
          width: "350px",
          backgroundColor: "#2b2b2b",
          border: "1px solid #ffa500",
          display: "flex",
          flexDirection: "column",
          gap: 2,
          padding: 5,
          borderRadius: 2,
          color: "#f0f0f0",
        }}
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
          type="email"
          fullWidth
          {...register("email", { required: "Email is required" })}
          error={!!errors.email}
          helperText={errors.email?.message}
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
          type="password"
          fullWidth
          {...register("password", { required: "Password is required" })}
          error={!!errors.password}
          helperText={errors.password?.message}
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
        <Link href="/register" color="#ffa500">
          Register here.
        </Link>
      </Box>
    </main>
  );
};

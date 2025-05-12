import { Link } from "@mui/material";

export const Navbar = () => {
  return (
    <nav>
      <ul className="flex gap-4 text-white">
        <li className="bg-orange-700 py-2 rounded-lg cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          <Link href="/login" color="inherit" underline="none" padding={2}>
            Login
          </Link>
        </li>
        <li className="bg-orange-700 py-2 rounded-lg cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          <a href="/register">
            <Link href="/register" color="inherit" underline="none" padding={2}>
              Create Account
            </Link>
          </a>
        </li>
      </ul>
    </nav>
  );
};

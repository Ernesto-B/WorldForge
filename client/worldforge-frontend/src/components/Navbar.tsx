import { Link } from "@mui/material";

export const Navbar = () => {
  return (
    <nav>
      <ul className="flex gap-4 text-white">
        <li className="py-2 px-6 bg-orange-700 rounded-lg cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          <Link href="/login">Log In</Link>
        </li>
        <li className="py-2 px-6 bg-orange-700 rounded-lg cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          <a href="/register">Sign Up</a>
        </li>
      </ul>
    </nav>
  );
};

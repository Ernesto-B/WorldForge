export const Navbar = () => {
  return (
    <nav>
      <ul className="flex gap-4 text-white">
        <li className="py-2 px-6 bg-orange-700 rounded-xl cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          Log In
        </li>
        <li className="py-2 px-6 bg-orange-700 rounded-xl cursor-pointer hover:bg-orange-800 hover:shadow-md transition-all">
          Sign Up
        </li>
      </ul>
    </nav>
  );
};

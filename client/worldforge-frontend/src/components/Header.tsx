import Logo from "../assets/logos/Logo.svg";
import { Navbar } from "./Navbar";

export const Header = () => {
  return (
    <header className="flex justify-between items-center p-4 bg-transparent">
      <img src={Logo} alt="worldforge" className="w-64" />
      <Navbar />
    </header>
  );
};

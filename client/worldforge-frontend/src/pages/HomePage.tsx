import logo from "../assets/logos/Logo.svg";

export const HomePage = () => {
  return (
    <>
      <div className="absolute w-full h-dvh bg-black opacity-50 z-10"></div>
      <div className="w-full h-dvh bg-[url(src/assets/images/dnd-wallpaper-1.jpg)] bg-no-repeat bg-cover relative">
        <header className="z-20 absolute left-60">
          <img src={logo} alt="logo" />
        </header>
        <nav className="p-8 z-20 absolute">
          <ul className="flex flex-col gap-8 w-fit">
            <li className="bg-gray-50 p-6 rounded">icon</li>
            <li className="bg-gray-50 p-6 rounded">icon</li>
            <li className="bg-gray-50 p-6 rounded">icon</li>
            <li className="bg-gray-50 p-6 rounded">icon</li>
          </ul>
        </nav>
        <div className="flex gap-4 absolute right-0 top-0 p-8 z-20">
          <button className="bg-gray-50 py-2 px-4 rounded-2xl">
            Create Campaign
          </button>
          <button className="bg-gray-50 py-2 px-4 rounded-2xl">
            Join Campaign
          </button>
        </div>
      </div>
    </>
  );
};

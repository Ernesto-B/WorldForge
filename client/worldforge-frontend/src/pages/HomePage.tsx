import { Header } from "../components/Header";
import background from "../assets/images/dnd-wallpaper-1.jpg";
import elf from "../assets/images/elf.png";

export const HomePage = () => {
  return (
    <div className="h-dvh bg-[#1b1b1b]">
      <Header />
      <section className="px-10 relative">
        <div className="relative w-full overflow-hidden">
          <img
            src={background}
            alt="hero-background"
            className="brightness-[60%] rounded-2xl rounded-bl-[200px] w-full h-[1000px] object-cover"
          ></img>
          <svg
            className="absolute bottom-0 left-0 w-full"
            viewBox="0 0 1440 320"
            preserveAspectRatio="none"
          >
            <path
              fill="#1b1b1b"
              fill-opacity="1"
              d="M0,192L80,186.7C160,181,320,171,480,154.7C640,139,800,117,960,117.3C1120,117,1280,139,1360,149.3L1440,160L1440,320L1360,320C1280,320,1120,320,960,320C800,320,640,320,480,320C320,320,160,320,80,320L0,320Z"
            ></path>
          </svg>
        </div>
        <div className="absolute right-0 top-60 w-[900px] h-auto pointer-events-none">
          <img src={elf} alt="elf" className="w-full h-auto object-contain" />
          <div className="absolute inset-0 bg-gradient-to-b from-transparent to-[#1b1b1b] to-[90%]"></div>
        </div>
        <p className="absolute top-[500px] left-[100px] text-white font-serif text-6xl w-1/2">
          Because even the <span className="text-orange-500">mightiest</span>{" "}
          heroes forget where they left the{" "}
          <span className="text-orange-500">map</span>.
        </p>
      </section>
    </div>
  );
};

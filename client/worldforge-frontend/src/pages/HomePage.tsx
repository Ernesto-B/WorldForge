import { Header } from "../components/Header";
import { Footer } from "../components/Footer";
import background from "../assets/images/dnd-wallpaper-1.jpg";
import elf from "../assets/images/elf.png";
import background2 from "../assets/images/bg2.png";
import background3 from "../assets/images/bg1.jpg";
import spectate from "../assets/images/dnd-spectate.avif";
import worldbuild from "../assets/images/dnd-worldbuild.avif";
import events from "../assets/images/dnd-worldevents.jpg";
import worldmap from "../assets/images/dnd-world-map.webp";
import fogofwar from "../assets/images/dnd-fogofwar.png";
import playeranddm from "../assets/images/dnd-worldbuilding.avif";
import dndMale from "../assets/images/dnd-character.png";
import dndFemale from "../assets/images/dnd-character-female.png";
import { Button, Typography } from "@mui/material";

export const HomePage = () => {
  return (
    <div className="min-h-fit bg-[#1b1b1b]">
      <Header />
      <main className="flex flex-col gap-40 px-10">
        <section className="relative overflow-hidden">
          <div className="relative w-full">
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
        <section className="bg-[#1b1b1b] flex gap-8">
          <img
            src={background2}
            className="w-1/2 h-[500px] shadow-black shadow-2xl rounded"
          />
          <div className="w-1/2 h-[500px] flex flex-col gap-4">
            <Typography
              variant="overline"
              fontSize="16px"
              color="white"
              fontWeight="bold"
            >
              What is WorldForge
            </Typography>
            <Typography variant="h2" fontSize="36px" color="white">
              A Living Atlas for Your D&D Campaigns
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              WorldForge transforms your campaign world into a dynamic,
              interactive map where every location tells a story. Whether you're
              a Dungeon Master managing lore or a player retracing epic quests,
              the map acts as the central hub for everything in your world —
              characters, session logs, locations, factions, and more.
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              Instead of scattered notes and fading memories, you get a
              visually-driven, persistent world that evolves with each session.
              Reveal new regions as players explore, track party movements, and
              log important events in a space everyone can revisit.
            </Typography>
            <Button
              variant="contained"
              sx={{
                bgcolor: "var(--color-orange-500)",
                fontWeight: "bold",
                fontSize: "16px",
                width: "fit-content",
                padding: "10px",
                marginTop: "20px",
                transition: "all 0.3s ease",
                "&:hover": {
                  bgcolor: "var(--color-orange-700)",
                },
              }}
            >
              Explore a Demo World
            </Button>
          </div>
        </section>
        <section className="bg-[#1b1b1b] flex gap-8">
          <div className="w-1/2 h-[500px] flex flex-col gap-4">
            <Typography
              variant="overline"
              fontSize="16px"
              color="white"
              fontWeight="bold"
            >
              Multi-Campaign, Shared World Support
            </Typography>
            <Typography variant="h2" fontSize="36px" color="white">
              Multiple Campaigns. One Living World
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              WorldForge lets you run multiple campaigns inside a single
              persistent world — perfect for long-term storytelling or
              collaborative universes. Whether you're juggling several parties
              or co-DMing with friends, each campaign has scoped visibility
              while still existing within the same evolving world.
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              You can track progress per group, synchronize global events, and
              even let players indirectly affect each other's stories through
              shared discoveries and outcomes.
            </Typography>
            <Button
              variant="contained"
              sx={{
                bgcolor: "var(--color-orange-500)",
                fontWeight: "bold",
                fontSize: "16px",
                width: "fit-content",
                padding: "10px",
                marginTop: "20px",
                transition: "all 0.3s ease",
                "&:hover": {
                  bgcolor: "var(--color-orange-700)",
                },
              }}
            >
              See How Campaign Sync Works
            </Button>
          </div>
          <img
            src={background3}
            className="w-1/2 h-[500px] shadow-black shadow-2xl object-cover rounded"
          />
        </section>
        <section className="grid grid-cols-3 mx-auto gap-20">
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={spectate}
              alt="characters spectating campaign"
              className="transition-all duration-500 h-80 object-cover group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-24 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                Spectator Access
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                Non-players follow along as spectators, viewing the world map
                and unlocked lore in real-time as sessions unfold.
              </p>
            </div>
          </div>
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={worldbuild}
              alt="characters building world"
              className="transition-all duration-500 h-80 object-cover object-right group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-28 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                Collaboritive Worldbuilding
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                Trusted collaborators contribute to the world’s development by
                adding lore entries, fleshing out regions, or populating cities
                with characters and shops.
              </p>
            </div>
          </div>
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={events}
              alt="characters fighting dragon for world event"
              className="transition-all duration-500 h-80 object-cover group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-24 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                World Events
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                DMs pin major world events that affect all campaigns, ensuring
                that global shifts in the setting are communicated across
                groups.
              </p>
            </div>
          </div>
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={worldmap}
              alt="world map"
              className="transition-all duration-500 h-80 object-cover group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-34 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                Interactive World Map
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                Explore a living world through an interactive map where every
                location links to rich content like lore, NPCs, and shops. The
                map evolves as your campaign progresses, revealing new regions
                and deepening immersion.
              </p>
            </div>
          </div>
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={fogofwar}
              alt="fog of war"
              className="transition-all duration-500 h-80 object-cover group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-28 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                Session Tracking & Fog of War
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                Track party journeys with hand-drawn session paths and
                dynamically reveal areas using a fog-of-war system. Each session
                becomes a visual story told across the map.
              </p>
            </div>
          </div>
          <div className="w-96 h-fit max-h-96 bg-[#2b2b2b] shadow-[#0b0b0b] shadow-2xl rounded overflow-hidden group">
            <img
              src={playeranddm}
              alt="player and dm contributions to map"
              className="transition-all duration-500 h-80 object-cover group-hover:brightness-75"
            />
            <div className="transition-all duration-500 group-hover:-translate-y-28 bg-[#2b2b2b]">
              <p className="text-[#f0f0f0] text-2xl font-semibold text-center py-4">
                Player & DM Contributions
              </p>
              <p className="p-4 pt-0 text-[#f0f0f0]">
                DMs control world visibility while players add personal markers
                and log sessions. Collaborators can expand the world with lore,
                characters, and more, all within clear role-based permissions.
              </p>
            </div>
          </div>
        </section>
        <section className="flex justify-center items-center h-[700px] relative">
          <div className="flex flex-col w-1/2 gap-6 items-center z-10">
            <h2 className="text-[#f0f0f0] font-semibold text-5xl">
              Begin Your Adventure Now!
            </h2>
            <p className="text-[#f0f0f0] text-xl text-center">
              Bring your world to life with a map that grows as your story
              unfolds. Whether you're a solo DM, part of a multi-party epic, or
              just starting your first campaign, WorldForge gives you the tools
              to track, build, and explore like never before. Visualize your
              sessions, collaborate with players, and craft a living world your
              group will never forget.
            </p>
            <p className="text-[#f0f0f0] text-2xl font-semibold">
              Sign up now and start forging your world.
            </p>
            <Button
              variant="contained"
              sx={{
                bgcolor: "var(--color-orange-500)",
                fontWeight: "bold",
                fontSize: "16px",
                width: "fit-content",
                padding: "10px",
                marginTop: "20px",
                transition: "all 0.3s ease",
                "&:hover": {
                  bgcolor: "var(--color-orange-700)",
                },
              }}
            >
              Create Account
            </Button>
          </div>
          <img
            className="absolute left-20 h-180 bottom-10 brightness-80"
            src={dndFemale}
            alt="D&D male character"
          />
          <img
            className="absolute right-20 h-180 bottom-10 brightness-80"
            src={dndFemale}
            alt="D&D female character"
          />
        </section>
      </main>
      <Footer />
    </div>
  );
};

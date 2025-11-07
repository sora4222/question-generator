import { QuestionGenerator } from "~/components/question-generator";
import type { Route } from "./+types/home";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Question Generator" },
    { name: "description", content: "Welcome to the Question Generator!" },
  ];
}

export default function Home() {
  return <QuestionGenerator />;
}

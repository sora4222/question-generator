import { Button } from "./ui/button";
import { Card, CardContent, CardDescription, CardHeader } from "./ui/card";

export function QuestionGenerator() {
  return (
    <main className="flex min-h-svh w-full items-center justify-center">
      <Card className="px-4 container my-1">
        <CardHeader>Generate Question</CardHeader>
        <CardDescription>
          A question about your learnings will be generated.
        </CardDescription>
        <CardContent className="items-center">
          <Button variant="default">Generate</Button>
        </CardContent>
      </Card>
    </main>
  );
}

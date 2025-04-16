import { describe, it, expect } from "vitest";
import { cn } from "./utils";

describe("cn utility function", () => {
  it("should combine basic class names correctly", () => {
    expect(cn("text-red-500")).toBe("text-red-500");
    expect(cn("text-red-500", "bg-blue-500")).toBe("text-red-500 bg-blue-500");
  });

  it("should handle conditional and falsy class names", () => {
    const isActive = true;
    const falseValue = false;
    expect(cn("base-class", isActive && "active-class")).toBe(
      "base-class active-class",
    );
    expect(cn("base-class", falseValue && "ignored-class")).toBe("base-class");
    expect(cn("base-class", undefined, null, 0, "")).toBe("base-class");
  });

  it("should properly merge Tailwind classes", () => {
    expect(cn("px-2 py-1", "p-3")).toBe("p-3");
    expect(cn("text-red-500", "text-blue-500")).toBe("text-blue-500");
  });
});

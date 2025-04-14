/**
 * Use this file only to keep shadcn's utility functions. There's currently
 * a bug where the value declared at `components.json` -> { "aliases": { "utils": "...", } }
 * is not being intepreted correctly by shadcn cli. So, we have to keep this file here.
 * This should be a temporary issue until the lib fixes it.
 */
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export interface GameEntry {
  name: string;
  year: number;
  platform: string;
  publisher: string;
  estimatedRevenue: number;
  revenueSource: string;
  confidence: "low" | "medium" | "high";
}

export interface ResearchOutput {
  games: GameEntry[];
  totalGamesFound: number;
  searchQueries: string[];
  sources: string[];
}

export interface ComparisonResult {
  iteration: number;
  similarityScore: number;
  gameCoverageScore: number;
  revenueAccuracyScore: number;
  matchedGames: number;
  totalUniqueGames: number;
  missingFromCLI: string[];
  missingFromSDK: string[];
  revenueDiscrepancies: {
    game: string;
    cliRevenue: number;
    sdkRevenue: number;
    percentDifference: number;
  }[];
  converged: boolean;
}

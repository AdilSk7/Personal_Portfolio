import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
    const { type } = req.query;
    let GITHUB_TOKEN = process.env.GITHUB_TOKEN;
    
    if (!GITHUB_TOKEN) {
        try {
            const envPath = path.join(process.cwd(), '.env.local');
            if (fs.existsSync(envPath)) {
                const envContent = fs.readFileSync(envPath, 'utf8');
                const match = envContent.match(/GITHUB_TOKEN\s*=\s*(.*)/);
                if (match) {
                    GITHUB_TOKEN = match[1].trim();
                }
            }
        } catch (e) {
            console.error("Local env parsing failed:", e);
        }
    }
    const GITHUB_USERNAME = "AdilSk7";

    if (!GITHUB_TOKEN) {
        return res.status(500).json({ error: "No GitHub token configured in Vercel Environment Variables" });
    }

    const headers = {
        "Authorization": `Bearer ${GITHUB_TOKEN}`,
        "Accept": "application/vnd.github+json"
    };

    try {
        if (type === 'profile') {
            const response = await fetch(`https://api.github.com/users/${GITHUB_USERNAME}`, { headers });
            if (!response.ok) {
                throw new Error(`GitHub Profile API returned ${response.status}`);
            }
            const data = await response.json();
            return res.status(200).json(data);
        } 
        
        if (type === 'repos') {
            // According to task, we should filter forks and get top 6 updated.
            const response = await fetch(`https://api.github.com/users/${GITHUB_USERNAME}/repos?sort=updated&direction=desc&per_page=100`, { headers });
            if (!response.ok) {
                throw new Error(`GitHub Repos API returned ${response.status}`);
            }
            let repos = await response.json();
            // Remove forks and slice top 6
            const topRepos = repos.filter(repo => !repo.fork).slice(0, 6);
            return res.status(200).json(topRepos);
        }

        return res.status(400).json({ error: "Invalid type parameter" });
    } catch (error) {
        console.error("Vercel Serverless Error:", error);
        return res.status(500).json({ error: error.message });
    }
}

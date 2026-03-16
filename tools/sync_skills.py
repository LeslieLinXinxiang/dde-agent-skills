#!/usr/bin/env python3
import os
import shutil
import argparse
import sys

def sync_skills(source, targets):
    """Sync skills from the repo structure to agent-specific directories."""
    if not os.path.exists(source):
        print(f"Error: Source directory {source} does not exist.")
        return

    for target in targets:
        target_path = os.path.expanduser(target)
        if not os.path.exists(target_path):
            print(f"Creating target directory: {target_path}")
            os.makedirs(target_path, exist_ok=True)

        print(f"Syncing to {target_path}...")
        for skill_name in os.listdir(source):
            src_skill = os.path.join(source, skill_name)
            if os.path.isdir(src_skill):
                dst_skill = os.path.join(target_path, skill_name)
                if os.path.exists(dst_skill):
                    shutil.rmtree(dst_skill)
                shutil.copytree(src_skill, dst_skill)
                print(f"  [SYNCED] {skill_name}")

def main():
    parser = argparse.ArgumentParser(description="Sync DDE skills from repository to agent environments.")
    parser.add_argument("--source", default="./skills", help="Source skills directory in repo")
    parser.add_argument("--targets", nargs="+", default=["~/.agents/skills", "~/.copilot/skills"], 
                        help="Target directories for syncing")
    
    args = parser.parse_args()
    sync_skills(args.source, args.targets)
    print("\nSync complete. Restart your agent session to load updated skills.")

if __name__ == "__main__":
    main()

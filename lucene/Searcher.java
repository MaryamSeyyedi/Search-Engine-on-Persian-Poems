/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package lucene;


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Date;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

/**
 * Simple command-line based search demo.
 */
public class Searcher {

    private Searcher() {
    }

    /**
     * Simple command-line based search demo.
     */
    public static void main(String[] args) throws Exception {

        String[] indexesDir = {
                "index/poems/raw",
                "index/poems/hazm/NT_hazm",
                "index/poems/hazm/NTR_hazm",
                "index/poems/hazm/NTRL_hazm",
                "index/poems/hazm/NTRS_hazm",
                "index/poems/parsivar/NT_parsivar",
                "index/poems/parsivar/NTR_parsivar",
                "index/poems/parsivar/NTRL_parsivar",
        };
        String[] queriesDir = {
                "dataset/queries/raw/",
                "dataset/queries/hazm/NT_hazm/",
                "dataset/queries/hazm/NTR_hazm/",
                "dataset/queries/hazm/NTRL_hazm/",
                "dataset/queries/hazm/NTRS_hazm/",
                "dataset/queries/parsivar/NT_parsivar/",
                "dataset/queries/parsivar/NTR_parsivar/",
                "dataset/queries/parsivar/NTRL_parsivar/",
        };

        String[] resultFiles = {
                "results/raw.txt",
                "results/NT_hazm.txt",
                "results/NTR_hazm.txt",
                "results/NTRL_hazm.txt",
                "results/NTRS_hazm.txt",
                "results/NT_parsivar.txt",
                "results/NTR_parsivar.txt",
                "results/NTRL_parsivar.txt",
        };

        String field = "contents";
        int repeat = 0;
        boolean raw = false;
        String queryString = null;
        int hitsPerPage = 10;
        Analyzer analyzer = new StandardAnalyzer();
        for (int indexCounter = 0; indexCounter < indexesDir.length; indexCounter++) {
            String index = indexesDir[indexCounter];
            IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(index)));
            IndexSearcher searcher = new IndexSearcher(reader);
            BufferedWriter writer = Files.newBufferedWriter(Paths.get(resultFiles[indexCounter]));
            for (int queryCounter = 1; queryCounter <= 47; queryCounter++) {
                writer.write(queryCounter + ".persian_query" + '\n');
                String queries = queriesDir[indexCounter] + queryCounter + ".persian_query";
                BufferedReader in = Files.newBufferedReader(Paths.get(queries), StandardCharsets.UTF_8);
                QueryParser parser = new QueryParser(field, analyzer);
                while (true) {
                    if (queries == null && queryString == null) {                        // prompt the user
                        System.out.println("Enter query: ");
                    }

                    String line = in.readLine();
                    String text = line;
                    while ((line = in.readLine()) != null) {
                        text += '\n' + line;
                    }
                    line = text;

                    if (line == null || line.length() == -1) {
                        break;
                    }

                    line = line.trim();
                    if (line.length() == 0) {
                        break;
                    }

                    Query query = parser.parse(line);
                    System.out.println("Searching for: " + query.toString(field));

                    if (repeat > 0) {                           // repeat & time as benchmark
                        Date start = new Date();
                        for (int i = 0; i < repeat; i++) {
                            searcher.search(query, 100);
                        }
                        Date end = new Date();
                        System.out.println("Time: " + (end.getTime() - start.getTime()) + "ms");
                    }

                    doPagingSearch(in, searcher, query, hitsPerPage, raw, queries == null && queryString == null, writer);

                    if (queryString != null) {
                        break;
                    }
                }
                writer.write('\n');
                writer.write('\n');
            }
            writer.close();
            reader.close();
        }

    }

    /**
     * This demonstrates a typical paging search scenario, where the search engine presents
     * pages of size n to the user. The user can then go to the next page if interested in
     * the next hits.
     * <p>
     * When the query is executed for the first time, then only enough results are collected
     * to fill 5 result pages. If the user wants to page beyond this limit, then the query
     * is executed another time and all hits are collected.
     */
    public static void doPagingSearch(BufferedReader in, IndexSearcher searcher, Query query,
                                      int hitsPerPage, boolean raw, boolean interactive, BufferedWriter writer) throws IOException {

        // Collect enough docs to show 5 pages
        TopDocs results = searcher.search(query, 5 * hitsPerPage);
        ScoreDoc[] hits = results.scoreDocs;

        int numTotalHits = Math.toIntExact(results.totalHits.value);
        System.out.println(numTotalHits + " total matching documents");
        writer.write(numTotalHits + " total matching documents" + '\n');

        int start = 0;
        int end = Math.min(numTotalHits, hitsPerPage);

        while (true) {
            if (end > hits.length) {
                System.out.println("Only results 1 - " + hits.length + " of " + numTotalHits + " total matching documents collected.");
                System.out.println("Collect more (y/n) ?");
                String line = in.readLine();
                if (line.length() == 0 || line.charAt(0) == 'n') {
                    break;
                }

                hits = searcher.search(query, numTotalHits).scoreDocs;
            }

            end = Math.min(hits.length, start + hitsPerPage);

            for (int i = start; i < end; i++) {
                if (raw) {                              // output raw format
                    System.out.println("doc=" + hits[i].doc + " score=" + hits[i].score);
                    continue;
                }

                Document doc = searcher.doc(hits[i].doc);
                String path = doc.get("path");
                if (path != null) {
                    System.out.println((i + 1) + ". " + path);
                    writer.write(Paths.get(path).getFileName().toString() + " ");
                    String title = doc.get("title");
                    if (title != null) {
                        System.out.println("   Title: " + doc.get("title"));
                    }
                } else {
                    System.out.println((i + 1) + ". " + "No path for this document");
                }

            }

            if (!interactive || end == 0) {
                break;
            }

            if (numTotalHits >= end) {
                boolean quit = false;
                while (true) {
                    System.out.print("Press ");
                    if (start - hitsPerPage >= 0) {
                        System.out.print("(p)revious page, ");
                    }
                    if (start + hitsPerPage < numTotalHits) {
                        System.out.print("(n)ext page, ");
                    }
                    System.out.println("(q)uit or enter number to jump to a page.");

                    String line = in.readLine();
                    if (line.length() == 0 || line.charAt(0) == 'q') {
                        quit = true;
                        break;
                    }
                    if (line.charAt(0) == 'p') {
                        start = Math.max(0, start - hitsPerPage);
                        break;
                    } else if (line.charAt(0) == 'n') {
                        if (start + hitsPerPage < numTotalHits) {
                            start += hitsPerPage;
                        }
                        break;
                    } else {
                        int page = Integer.parseInt(line);
                        if ((page - 1) * hitsPerPage < numTotalHits) {
                            start = (page - 1) * hitsPerPage;
                            break;
                        } else {
                            System.out.println("No such page");
                        }
                    }
                }
                if (quit) break;
                end = Math.min(numTotalHits, start + hitsPerPage);
            }
        }
    }
}